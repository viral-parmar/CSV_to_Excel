import sys
from PyQt5 import QtCore, QtGui, uic

qtCreatorFile = "csvExcel.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())