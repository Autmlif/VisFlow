import sys, os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qtrangeslider import QLabeledRangeSlider

# from Resource import images_rc
import matplotlib as mpl

mpl.use("Qt5Agg")
import numpy as np


# 流场基本绘制的对话框
#


class ContoursDataPlotOptionDialog(QDialog):
    def __init__(self, data_range, call_back_draw=None, parent=None):
        super(ContoursDataPlotOptionDialog, self).__init__(parent)
        self.setMinimumSize(500, 450)
        self.setMaximumSize(700, 650)
        self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowIcon(QIcon(':/png/icon/contour_option.png'))
        # self._layout_init()
        self.setupUi(self, data_range)

        self.pushButton.clicked.connect(self.displayAction)

        # draw call back function
        self.draw_handler = call_back_draw

    def setupUi(self, Form, data_range):
        Form.setObjectName("Form")
        Form.resize(649, 385)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(11, 11, -1, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_6.addWidget(self.checkBox_3)
        self.range_slider = QLabeledRangeSlider()
        self.range_slider.setOrientation(Qt.Horizontal)
        self.range_slider.setMinimum(data_range[0])
        self.range_slider.setMaximum(data_range[1])
        self.range_slider.setValue(data_range)
        self.horizontalLayout_6.addWidget(self.range_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Contour"))
        self.groupBox.setTitle(_translate("Form", "等值面"))
        self.checkBox.setText(_translate("Form", "显示原图"))
        self.checkBox_2.setText(_translate("Form", "指定等值面数量"))
        self.checkBox_3.setText(_translate("Form", "指定划分范围"))
        self.label_2.setText(_translate("Form", "筛选方法"))
        self.comboBox.setItemText(0, _translate("Form", "contour"))
        self.comboBox.setItemText(1, _translate("Form", "marching_cubes"))
        self.comboBox.setItemText(2, _translate("Form", "flying_edges"))
        self.label_4.setText(_translate("Form", "透明度"))
        self.pushButton.setText(_translate("Form", "绘制"))
        self.pushButton_2.setText(_translate("Form", "取消"))

        # # event define
        # self.btn_display.clicked.connect(self.displayAction)

    def displayAction(self):
        # print("disp")
        data = {"display_mesh": self.checkBox.isChecked(),
                "specify_iso": self.checkBox_2.isChecked(),
                "iso_numbers": self.spinBox.value(),
                "specify_range": self.checkBox_3.isChecked(),
                "iso_range": (self.range_slider.value()),
                "screening_tech": self.comboBox.currentText(),
                "opacity": self.doubleSpinBox.value(),
                }
        self.draw_handler(data)


class VolumePlotOptionDialog(QDialog):
    def __init__(self, call_back_draw=None, parent=None):
        super(VolumePlotOptionDialog, self).__init__(parent)
        # self.setMinimumSize(500, 450)
        # self.setMaximumSize(700, 650)
        # self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowIcon(QIcon(':/png/icon/volume_option.png'))
        self.setupUi(self)

        self.draw_handler = call_back_draw
        self.init_widget()

    def init_widget(self):
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.valueChanged.connect(lambda: self.label_2.setText(str(self.horizontalSlider.value()/1000)))
        self.pushButton.clicked.connect(self.displayAction)

    def displayAction(self):
        data = {"display_grid": self.checkBox.isChecked(),
                "voxel_size": self.horizontalSlider.value()/1000,
                "opacity": self.doubleSpinBox.value(),
                }
        self.draw_handler(data)

    def setupUi(self, volume_window):
        volume_window.setObjectName("volume_window")
        volume_window.resize(373, 381)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(volume_window)
        self.verticalLayout_2.setContentsMargins(11, 11, -1, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(volume_window)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(volume_window)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(volume_window)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(volume_window)
        QtCore.QMetaObject.connectSlotsByName(volume_window)

    def retranslateUi(self, volume_window):
        _translate = QtCore.QCoreApplication.translate
        volume_window.setWindowTitle(_translate("volume_window", "Volume"))
        self.groupBox.setTitle(_translate("volume_window", "Voxelize"))
        self.checkBox.setText(_translate("volume_window", "显示网格"))
        self.label_4.setText(_translate("volume_window", "透明度"))
        self.label.setText(_translate("volume_window", "Voxel Size"))
        self.label_2.setText(_translate("volume_window", "0.01"))
        self.pushButton.setText(_translate("volume_window", "绘制"))
        self.pushButton_2.setText(_translate("volume_window", "取消"))

class MeshOptionDialog(QDialog):
    def __init__(self, varNames=[], zoneNames=[], call_back_draw=None, parent=None):
        super(MeshOptionDialog, self).__init__(parent)
        self.setMinimumSize(500, 450)
        self.setMaximumSize(700, 650)
        self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowTitle('Mesh')
        self.setWindowIcon(QIcon(':/png/icon/mesh_option.png'))
        self._layout_init()

        # data init
        self.zoneNames = zoneNames
        self.comb_varible.addItems(varNames)
        qlm = QStringListModel(zoneNames)
        self.list_zone_surface.setModel(qlm)
        self.list_zone_surface.setCurrentIndex(qlm.index(0, 0))
        # draw call back function
        self.draw_handler = call_back_draw

        # event define
        self.btn_display.clicked.connect(self.displayAction)

    def displayAction(self):
        # print("disp")
        data = {"name": self.le_name.text(),
                "style": self.comb_style.currentText(),
                "mesh": self.check_mesh.isChecked(),
                "smooth": self.check_smooth.isChecked(),
                "log_scale": self.check_logScale.isChecked(),
                "colormap": self.comb_colormap_style.currentText(),
                "colormapsize": self.spin_colormap_size.value(),
                "varName": self.comb_varible.currentText(),
                "zoneName": [item.data() for item in self.list_zone_surface.selectedIndexes()]
                }
        self.draw_handler(data)

    def _layout_init(self):
        # 纵向布局
        layout_out = QVBoxLayout()
        layout_out.setContentsMargins(20, 10, 20, 10)
        layout_out.setSpacing(10)
        # 第一行
        layout_row1 = QHBoxLayout()
        layout_row1.addWidget(QLabel("绘图名"))
        self.le_name = QLineEdit(self)
        layout_row1.addWidget(self.le_name)
        layout_out.addLayout(layout_row1)

        # 第二行
        layout_row2 = QHBoxLayout()
        layout_row2_left = QVBoxLayout()
        layout_row2_right = QVBoxLayout()
        layout_row2.addLayout(layout_row2_left)
        layout_row2.addLayout(layout_row2_right)
        layout_out.addLayout(layout_row2)

        group_option = QGroupBox("选项")
        layout_row2_left.addWidget(group_option)
        layout_option = QVBoxLayout()
        group_option.setLayout(layout_option)

        self.comb_style = QComboBox()
        self.comb_style.addItems(["surface", "points", "wireframe"])  # ``style='surface'``, ``style='wireframe'``, ``style='points'``, ``style='points_gaussian'``
        # self.check_filled = QCheckBox("填充")
        # self.check_filled.setChecked(True)
        self.check_mesh = QCheckBox("显示网格")
        self.check_smooth = QCheckBox("平滑")

        layout_option.addWidget(self.comb_style)
        layout_option.addWidget(self.check_mesh)
        layout_option.addWidget(self.check_smooth)

        group_colormap = QGroupBox("Colormap")
        layout_row2_left.addWidget(group_colormap)
        layout_colormap = QVBoxLayout()
        group_colormap.setLayout(layout_colormap)

        self.check_logScale = QCheckBox("取Log值")
        layout_colormap.addWidget(self.check_logScale)
        layout_colormap.addWidget(QLabel("分段数"))
        self.spin_colormap_size = QSpinBox()
        self.spin_colormap_size.setValue(10)
        layout_colormap.addWidget(self.spin_colormap_size)
        layout_colormap.addWidget(QLabel("风格"))
        self.comb_colormap_style = ColormapChoser()
        layout_colormap.addWidget(self.comb_colormap_style)

        layout_row2_right.addWidget(QLabel("变量"))
        self.comb_varible = QComboBox()
        layout_row2_right.addWidget(self.comb_varible)
        self.list_zone_surface = QListView()
        self.list_zone_surface.setSelectionMode(QAbstractItemView.MultiSelection)

        layout_row2_right.addWidget(QLabel("Zone"))
        layout_row2_right.addWidget(self.list_zone_surface)

        # 第四行
        layout_row4 = QHBoxLayout()
        self.btn_display = QPushButton("绘制")
        self.btn_cancel = QPushButton("取消")
        layout_row4.addStretch()
        layout_row4.addWidget(self.btn_display)
        layout_row4.addWidget(self.btn_cancel)
        layout_row4.addStretch()
        layout_row4.setSpacing(20)
        layout_out.addLayout(layout_row4)

        self.setLayout(layout_out)


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


##
# 定义colormap组件
class ColormapChoser(QWidget):
    def __init__(self):
        super(ColormapChoser, self).__init__()
        self.setMinimumSize(40, 20)
        self.fig = Figure(figsize=(3, 0.35), dpi=100)
        self.ax = self.fig.subplots(nrows=1)
        self.fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
        gradient = np.linspace(0, 1, 256)
        self.gradient = np.vstack((gradient, gradient))
        self.ax.set_axis_off()
        self.ax.imshow(self.gradient, aspect='auto', cmap=mpl.colormaps["viridis"])
        layout = QVBoxLayout()
        self.combo_stylename = QComboBox()
        self.combo_stylename.addItems(mpl.colormaps.keys())
        self.combo_stylename.setCurrentText("viridis")
        self.figCanvas = FigureCanvas(self.fig)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.combo_stylename)
        layout.addWidget(self.figCanvas)
        self.setLayout(layout)

        self.combo_stylename.currentTextChanged.connect(self.selectionchange)

    # 返回当前选择
    def currentText(self):
        return self.combo_stylename.currentText()

    def selectionchange(self, style_name):
        self.plot(style_name)

    def plot(self, colormap_name):
        self.ax.imshow(self.gradient, aspect='auto', cmap=mpl.colormaps[colormap_name])
        self.figCanvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)


    def fun(data):
        print(data)


    cDemo = MeshOptionDialog(varNames=["a", "b", "c"], zoneNames=["aaa", "bbb"], call_back_draw=fun)
    cDemo.show()
    sys.exit(app.exec_())
