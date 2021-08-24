from flask import Flask, request, send_file, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import zipfile
import secrets
import re
import html
import os
import io
from base import Session, engine, Base
from models import User, UserSongs, MusicCategories


REGEX = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
UPLOAD_FOLDER = 'C:/Users/mrocz/PycharmProjects/FLASKAPPTEST/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3'}
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Base.metadata.create_all(engine)
session = Session()


def validate(pass_to_check):
    if len(pass_to_check) < 8:
        return {"result": False, "message": "Make sure your password is at lest 8 letters"}
    elif re.search('[0-9]', pass_to_check) is None:
        return {"result": False, "message": "Make sure your password has a number in it"}
    elif re.search('[A-Z]', pass_to_check) is None:
        return {"result": False, "message": "Make sure your password has a capital letter in it"}
    else:
        return {"result": True, "message": "Your password seems fine"}


def check(email):
    if re.search(REGEX, email):
        return True
    else:
        return False


def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/register', methods=['GET', 'POST'])
def register():
    data = request.form.to_dict()
    if not check(data['email']):
        return {"error": "2", "message": "Invalid email address"}
    # validation = validate(data["password"])
    # if not validation["result"]:
        # return {"error": "2", "message": validation["message"]}
    email_check = session.query(User).filter_by(email=data["email"]).first()
    username_check = session.query(User).filter_by(username=data["username"]).first()
    if email_check:
        return {"error": "2", "message": "Account registered on this email address already exists"}
    if username_check:
        return {"error": "2", "message": "User with that name already exists"}
    hashed_password = generate_password_hash(data['password'], method="pbkdf2:sha256", salt_length=8)
    hashed_name = generate_password_hash(data['username'], method="pbkdf2:sha256", salt_length=8)
    new_user = User(
        email=data['email'],
        username=data['username'],
        password=hashed_password,
        hashed_name=hashed_name,
        token=""
    )
    dir_name = UPLOAD_FOLDER + '/' + data['username']
    os.mkdir(dir_name)
    print("Directory ", dir_name, " Created ")
    # add additional validations
    session.add(new_user)
    session.commit()
    return {"error": "1", "message": "Success"}


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form.to_dict()
    email = html.escape(data['email'])
    password = html.escape(data['password'])
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return {"error": "2", "message": "Wrong email"}
    if not check_password_hash(user.password, password):
        return {"error": "3", "message": "Wrong password"}
    token = secrets.token_hex(16) + " "
    tokens = user.token
    list_of_tokens = tokens.split()
    if len(list_of_tokens) > 2:
        list_of_tokens = list_of_tokens[1:]
    list_of_tokens.append(token)
    tokens = convert_list_to_string(list_of_tokens) + " "
    user.token = tokens
    session.commit()
    return {"error": "1", "token": token, "hashed_name": user.hashed_name, "message": "Successfully logged in(credentials)"}


@app.route('/login_t', methods=['GET', 'POST'])
def login_t():
    data = request.form.to_dict()
    token = data['token']
    hashed_name = data['hashed_name']
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        tokens = user.token
        list_of_tokens = tokens.split()
        if token in list_of_tokens:
            return {"error": "1", "message": "Successfully logged in(token)"}
        else:
            return {"error": "2", "message": "Token not found"}
    else:
        return {"error": "3", "message": "User not found"}


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    data = request.form.to_dict()
    token = data['token']
    hashed_name = data['hashed_name']
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        tokens = user.token
        list_of_tokens = tokens.split()
        if token in list_of_tokens:
            list_of_tokens.remove(token)
            tokens = convert_list_to_string(list_of_tokens) + " "
            user.token = tokens
            session.commit()
            return {"error": "1", "message": "Logged out"}
        else:
            return {"error": "2", "message": "Token not found"}
    else:
        return {"error": "3", "message": "User not found"}


@app.route('/add_song', methods=['GET', 'POST'])
def add_song():
    hashed_name = request.json["hashed_name"]
    songs = request.json["songs"]
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    user_songs = session.query(UserSongs).filter_by(user_id=user.id).all()
    titles = []
    for song in user_songs:
        titles.append(song.title)
    if user:
        updated_songs_id = []
        for i in songs:
            # TODO
            # change filtering by title to something else
            if i["title"] not in titles:
                updated_songs_id.append(i["id"])
                new_song = UserSongs(
                    title=i["title"],
                    author=i["author"],
                    category=i["category"],
                    user=user,
                    song_id=i["id"],
                    file_path=""
                )
                session.add(new_song)
        session.commit()
        if len(updated_songs_id) == 0:
            return {"error": "1", "message": "Everything is up to date", "updated_songs_id": updated_songs_id}
        else:
            return {"error": "1", "message": "Song added FLASK", "updated_songs_id": updated_songs_id}
    return {"error": "2", "message": "User not found"}


@app.route('/is_logged_in', methods=['GET', 'POST'])
def is_logged_in():
    data = request.form.to_dict()
    token = data['token']
    hashed_name = data['hashed_name']
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        tokens = user.token
        list_of_tokens = tokens.split()
        if token in list_of_tokens:
            return {"error": "1", "message": "You are logged in"}
        else:
            return {"error": "2", "message": "Token not found"}
    else:
        return {"error": "3", "message": "User not found"}


@app.route('/upload_files', methods=['GET', 'POST'])
def upload_files():
    data = request.form.to_dict(flat=False)
    hashed_name = data["hashed_name"][0]
    songs_ids = data["songs_ids"]
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        index = 0
        files = request.files.getlist("file")
        for file in files:
            filename = secure_filename(file.filename)
            if filename != "":
                song_id = songs_ids[index]
                song = session.query(UserSongs).filter_by(song_id=song_id).first()
                if song:
                    index += 1
                    user_folder_path = "/" + user.username
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'] + user_folder_path, filename))
                    song.file_path = app.config['UPLOAD_FOLDER'] + user_folder_path + "/" + filename
                else:
                    return {"error": "2", "message": "Error (SONG ID NOT FOUND)"}
        session.commit()
        return {"error": "1", "message": "Successfully uploaded files"}
    else:
        session.commit()
        return {"error": "2", "message": "User not found"}


@app.route('/download_files', methods=["GET", "POST"])
def download_files():
    data = request.form.to_dict(flat=False)
    hashed_name = data["hashed_name"][0]
    status = data["is_empty"][0]
    if status == "True":
        all_ids = []
    else:
        all_ids = [int(numeric_string) for numeric_string in data["all_ids"]]
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        user_songs = session.query(User).filter_by(user_id=user.id).all()
        missing_ids = []
        for item in user_songs:
            if item.song_id not in all_ids:
                missing_ids.append(item.song_id)
        missing_songs = session.query(UserSongs).filter(UserSongs.song_id.in_(missing_ids)).all()
        data = io.BytesIO()
        with zipfile.ZipFile(data, mode='w') as zf:
            for i in missing_songs:
                filename = os.path.basename(i.file_path)
                zf.write(i.file_path, filename)
        data.seek(0)
        return send_file(data, download_name='data.zip')


@app.route('/missing_songs_data', methods=["GET", "POST"])
def missing_songs_data():
    data = request.form.to_dict(flat=False)
    hashed_name = data["hashed_name"][0]
    status = data["is_empty"][0]
    if status == "True":
        all_ids = []
    else:
        all_ids = [int(numeric_string) for numeric_string in data["all_ids"]]
    user = session.query(User).filter_by(hashed_name=hashed_name).first()
    if user:
        user_songs = session.query(UserSongs).filter_by(user_id=user.id).all()
        missing_songs = []
        for item in user_songs:
            if item.song_id not in all_ids:
                filename = os.path.basename(item.file_path)
                dict_temp = {"title": item.title, "author": item.author, "cat": item.category, "filename": filename, "song_id": item.song_id}
                missing_songs.append(dict_temp)
        return jsonify(missing_songs)
    # zmienic tego returna
    return ""


@app.route('/get_music_categories')
def get_music_categories():
    music_categories = session.query(MusicCategories).all()
    if music_categories:
        music_categories_list = []
        for i in music_categories:
            music_categories_list.append(i.category_name)
        return {"error": "1", "data": music_categories_list}
    else:
        return {"error": "2", "message": "Error while getting music categories"}


@app.route("/get_songs_by_category", methods=["GET", "POST"])
def get_songs_by_category():
    data = request.form.to_dict()
    songs_by_category = session.query()

if __name__ == "__main__":
    app.run(debug=True)
