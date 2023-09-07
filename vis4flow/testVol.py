import sys

# Setting the Qt bindings for QtPy
import os

from VisWindow import VisWindow

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
        meshMenu = mainMenu.addMenu('Draw')
        self.draw_action = QtWidgets.QAction('Mesh', self)
        self.draw_action.triggered.connect(lambda: self.drawAction("mesh"))
        meshMenu.addAction(self.draw_action)

        self.draw_action_2 = QtWidgets.QAction('Iso-Surfaces', self)
        self.draw_action_2.triggered.connect(lambda: self.drawAction("contour"))
        meshMenu.addAction(self.draw_action_2)

        self.draw_action_3 = QtWidgets.QAction('Volume', self)
        self.draw_action_3.triggered.connect(lambda: self.drawAction("volume"))
        meshMenu.addAction(self.draw_action_3)

        self.draw_action_4 = QtWidgets.QAction('Slice', self)
        self.draw_action_4.triggered.connect(lambda: self.drawAction("slice"))
        meshMenu.addAction(self.draw_action_4)

        # self.drawAction()

        self.show()

    def drawAction(self, mesh):
        self.visWin.drawDialg(mesh)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    sys.exit(app.exec_())