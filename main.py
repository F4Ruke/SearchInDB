from logic import Logic, QtWidgets, book
from sys import argv

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = Logic()
    window.show()
    app.exec()
    book.close()
