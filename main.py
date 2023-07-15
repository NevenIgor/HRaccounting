from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.menubar = QtWidgets.QMenuBar(self)

        self.centralwidget = QtWidgets.QWidget()

        self.statusbar = QtWidgets.QStatusBar(self)

        self.setCentralWidget(self.centralwidget)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
