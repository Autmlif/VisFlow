import sys

# Setting the Qt bindings for QtPy
import os

from UI.File.Vis4Flow.VisWindow import VisWindow

os.environ["QT_API"] = "pyqt5"

from qtpy import QtWidgets

# from Vis4Flow.VisWindow import VisWindow

from pyvistaqt import QtInteractor, MainWindow

class MyMainWindow(MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # create the frame
        self.visWin = VisWindow()
        vlayout = QtWidgets.QVBoxLayout()

        self.setCentralWidget(self.visWin)

        # menu
        mainMenu = self.menuBar()
        # draw
        meshMenu = mainMenu.addMenu('draw')
        self.draw_action = QtWidgets.QAction('draw', self)
        meshMenu.addAction(self.draw_action)
        self.draw_action.triggered.connect(self.drawAction)
        # self.drawAction()

        self.show()

    def drawAction(self):
        self.visWin.drawDialg()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    sys.exit(app.exec_())