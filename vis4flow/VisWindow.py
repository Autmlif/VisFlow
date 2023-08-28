import math
import sys

# Setting the Qt bindings for QtPy
import os

import pyvista
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

os.environ["QT_API"] = "pyqt5"
import TecplotSzplt as tecplt
from visDialog import MeshOptionDialog
from visDialog import ContoursDataPlotOptionDialog
from visDialog import VolumePlotOptionDialog

from qtpy import QtWidgets

import matplotlib as mpl

import numpy as np

import pyvista as pv
from pyvistaqt import QtInteractor, MainWindow

from scipy.spatial import KDTree

class VisWindow(MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        # check whether the mesh has been drawn.
        self.mesh_range = None
        self.scalar_bar_args = None
        self.mesh_drawn = 0
        self.mesh_data = None

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

    def drawDialg(self, draw_type):
        if not hasattr(self, "tecData") or self.tecData == None:
            self.loadData()

        zonenames = self.tecData.getZoneNames()
        varNames = self.tecData.getVarNames()
        if draw_type == 'mesh':
            self.mDemo = MeshOptionDialog(varNames=varNames, zoneNames=zonenames, call_back_draw=self.paint_mesh)
            self.mDemo.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.mDemo.show()
        elif draw_type == 'contour':
            if self.mesh_drawn == 0:
                msg_box = QMessageBox(QMessageBox.Information, '提示', '请先选择绘制的场和变量。')
                msg_box.exec_()
            else:
                self.cDemo = ContoursDataPlotOptionDialog(data_range=self.mesh_range, call_back_draw=self.paint_contour)
                self.cDemo.setWindowFlag(Qt.WindowStaysOnTopHint)
                self.cDemo.show()
        elif draw_type == 'volume':
            self.vDemo = VolumePlotOptionDialog(call_back_draw=self.paint_volume)
            self.vDemo.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.vDemo.show()

    def paint_mesh(self, data):
        # data = {"name","filled","mesh","smooth","colormap","colormapsize","varName","zoneName"}
        print(data)

        self.scalar_bar_args = dict(
            interactive=True, title_font_size=20, label_font_size=16,
            shadow=True, n_labels=data['colormapsize'],
            italic=True,  font_family="arial",
            width=0.01, height=0.5
        )
        self.plotter.clear()

        self.mesh_data = []
        mesh_range_min = []
        mesh_range_max = []
        for zoneName in data["zoneName"]:
            mesh = self.tecData.getZoneVista(zoneName)  # 切换不同的zone
            mesh.set_active_scalars(data["varName"], preference='cell')  # 切换不同的变量，即不同的场

            # 求出数据范围
            scalar_min = mesh.active_scalars.min()
            scalar_max = mesh.active_scalars.max()
            mesh_range_min.append(scalar_min)
            mesh_range_max.append(scalar_max)

            # voxels = pv.voxelize(mesh, density=0.005)
            # voxels.compute_implicit_distance(mesh, inplace=True)
            # contours = voxels.contour(6, scalars="implicit_distance")
            # voxels["density"] = data["varName"]
            # glyphs = voxels.glyph(factor=1e-3, geom=pv.Arrow())


            #self.plotter.add_mesh(voxels, color=True, show_edges=True, opacity=0.25)
            # self.plotter.add_mesh(contours, color=True, show_edges=True, opacity=0.5)
            #slices = mesh.slice_orthogonal(x=0.5, y=0.5, z=0.5)
            #self.plotter.add_mesh(slices, cmap=mpl.colormaps[data["colormap"]])
            # mesh['scalars']=data["varName"]
            self.plotter.add_mesh(mesh, show_edges=data['mesh'], cmap=mpl.colormaps[data["colormap"]],
                                  log_scale=data['log_scale'], style=data['style'],
                                  smooth_shading=data['smooth'], scalar_bar_args=self.scalar_bar_args)
            # self.plotter.add_volume(mesh)
            #self.plotter.add_mesh(contours,  opacity=0.25)
            # self.plotter.add_volume(mesh, cmap=mpl.colormaps[data["colormap"]],
            #                         diffuse=1, log_scale=data['log_scale'],
            #                         e=0.0001)
        # self.plotter.add_mesh_slice(mesh, normal='z')
            self.mesh_data.append(mesh)

        self.mesh_range = [math.floor(min(mesh_range_min)), math.ceil(max(mesh_range_max))]

        self.plotter.reset_camera()
        self.mesh_drawn = 1

    def paint_contour(self, data):
        print(data)

        if not data['display_mesh']:
            self.plotter.clear()

        for mesh in self.mesh_data:
            mesh_points = mesh.cell_data_to_point_data()
            contours = mesh_points.contour(data['iso_numbers']) if data['specify_iso'] else mesh_points.contour()
            self.plotter.add_mesh(contours, opacity=data['opacity'], clim=data['iso_range'])
        self.plotter.reset_camera()

    def paint_volume(self, data):
        print(data)
        self.plotter.clear()
        for mesh in self.mesh_data:
            voxels = calculate_neighbours(mesh, data['voxel_size'])
            self.plotter.add_mesh_threshold(voxels, show_edges=data['display_grid'], opacity=data['opacity'])
        self.plotter.reset_camera()

# 计算体素半径
def calculate_sphere_radius(voxel_size):
    voxel_volume = voxel_size ** 3
    radius = ((3*voxel_volume)/(4*np.pi))**(1/3)
    return radius


def calculate_neighbours(mesh, voxel_size=0.01):
    # voxelize the given mesh with a specified size voxels
    voxels = pv.voxelize(mesh, density=voxel_size, check_surface=False)
    # Get the voxel center points
    voxel_centers = voxels.cell_centers().points
    # Get the mesh vertices
    mesh_vertices = mesh.points
    # Calculate the KDTree of the mesh vertices from Scipy
    kd_tree_vertices = KDTree(mesh_vertices)
    # Call the sphere radius function and calculate the new radius
    radius = calculate_sphere_radius(voxel_size)
    # Use the calculated KDTree and radius to get the neighbors for each voxel center
    neighbours = kd_tree_vertices.query_ball_point(voxel_centers,radius)
    # Count the number of points for each voxel center
    neighbour_count = [len(curr_neighbours) for curr_neighbours in neighbours]
    # Cast to array and normalize between 0 and 1
    neighbour_count = np.array(neighbour_count, dtype=np.float32)
    neighbour_density =  neighbour_count/neighbour_count.max()
    # Add the density as a field to the voxels
    voxels['density'] = neighbour_density

    return voxels

if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # window = VisWindow()
    # window.show()
    # sys.exit(app.exec_())
    pass