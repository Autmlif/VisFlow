import sys

# Setting the Qt bindings for QtPy
import os

from PyQt5.QtCore import Qt

os.environ["QT_API"] = "pyqt5"
from UI.File.Vis4Flow import TecplotSzplt as tecplt
from UI.File.Vis4Flow.visDialog import ContoursOptionDialog

from qtpy import QtWidgets

import numpy as np

import pyvista as pv
from pyvistaqt import QtInteractor, MainWindow

class VisWindow(MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # create the frame
        self.frame = QtWidgets.QFrame()
        vlayout = QtWidgets.QVBoxLayout()

        # add the pyvista interactor object
        self.plotter = QtInteractor(self.frame)
        # self.plotter = exampleDetails.plotter
        vlayout.addWidget(self.plotter.interactor)
        self.signal_close.connect(self.plotter.close)

        self.frame.setLayout(vlayout)
        self.setCentralWidget(self.frame)
        self.path = os.path.dirname(os.path.abspath(__file__))

        # # menu
        # mainMenu = self.menuBar()
        # # draw
        # meshMenu = mainMenu.addMenu('draw')
        # self.draw_action = QtWidgets.QAction('draw', self)
        # meshMenu.addAction(self.draw_action)
        # self.draw_action.triggered.connect(self.drawDialg)
        # self.show()

    def loadData(self):
        self.tecData = tecplt.read(os.path.join(self.path, "flow000002.szplt"))

    def drawDialg(self):
        if not hasattr(self, "tecData") or self.tecData == None:
            self.loadData()

        zonenames = self.tecData.getZoneNames()
        varNames = self.tecData.getVarNames()
        self.cDemo = ContoursOptionDialog(varNames=varNames, zoneNames=zonenames, call_back_draw=self.paintdata)
        self.cDemo.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.cDemo.show()

    def paintdata(self, data):
        # data = {"name","filled","mesh","smooth","colormap","colormapsize","varName","zoneName"}
        print(data)

        scalar_bar_args = dict(
            interactive=True, title_font_size=20, label_font_size=16,
            shadow=True, n_labels=data['colormapsize'],
            italic=True,  font_family="arial",
            width=0.01, height=0.5
        )
        import matplotlib as mpl
        self.plotter.clear()
        for zoneName in data["zoneName"]:
            mesh = self.tecData.getZoneVista(zoneName)  # 切换不同的zone
            mesh.set_active_scalars(data["varName"],preference='cell')  # 切换不同的变量，即不同的场
            # mesh['scalars']=data["varName"]
            self.plotter.add_mesh(mesh, show_edges=data['mesh'], cmap=mpl.colormaps[data["colormap"]],
                                  log_scale=data['log_scale'], style=data['style'],
                                  smooth_shading=data['smooth'], scalar_bar_args=scalar_bar_args)

            # self.plotter.add_volume(mesh, cmap=mpl.colormaps[data["colormap"]],
            #                         diffuse=1, log_scale=data['log_scale'],
            #                         e=0.0001)
        # self.plotter.add_mesh_slice(mesh, normal='z')
        self.plotter.reset_camera()


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # window = VisWindow()
    # window.show()
    # sys.exit(app.exec_())
    pass