import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from app_view import Ui_MainWindow
from app_controller import Controller


def main():
    app = QApplication(sys.argv)
    window = QMainWindow(parent=None)
    ui = Ui_MainWindow(window)
    controller = Controller(ui)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
