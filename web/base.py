from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = "postgres"
db_password = "password"
engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost:5432/PeachPlayer')
Session = sessionmaker(bind=engine)

Base = declarative_base()