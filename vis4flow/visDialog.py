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
    def __init__(self, varNames=[], zoneNames=[], call_back_draw=None, parent=None):
        super(ContoursDataPlotOptionDialog, self).__init__(parent)
        self.setMinimumSize(500, 450)
        self.setMaximumSize(700, 650)
        # self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowIcon(QIcon(':/png/icon/contour_option.png'))
        # self._layout_init()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.displayAction)

        # data init
        self.comboBox_style.addItems(["surface", "points", "wireframe"])

        self.zoneNames = zoneNames
        self.comboBox_variable.addItems(varNames)
        qlm = QStringListModel(zoneNames)
        self.list_zone_surface.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_zone_surface.setModel(qlm)
        self.list_zone_surface.setCurrentIndex(qlm.index(0, 0))

        # draw call back function
        self.draw_handler = call_back_draw

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 693)
        self.verticalLayout_entirety = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_entirety.setObjectName("verticalLayout_entirety")

        # 第一行
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_name = QtWidgets.QLabel(Form)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        self.text_plot_name = QtWidgets.QLineEdit(Form)
        self.text_plot_name.setObjectName("text_plot_name")
        self.horizontalLayout.addWidget(self.text_plot_name)
        self.verticalLayout_entirety.addLayout(self.horizontalLayout)

        #第二行
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_style = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_style.setObjectName("comboBox_style")
        self.verticalLayout_3.addWidget(self.comboBox_style)
        self.checkBox_grid = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_grid.setObjectName("checkBox_grid")
        self.verticalLayout_3.addWidget(self.checkBox_grid)
        self.checkBox_smooth = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_smooth.setObjectName("checkBox_smooth")
        self.verticalLayout_3.addWidget(self.checkBox_smooth)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_log = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_log.setObjectName("checkBox_log")
        self.verticalLayout_4.addWidget(self.checkBox_log)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.spin_colormap = QtWidgets.QSpinBox(self.groupBox_3)
        self.spin_colormap.setProperty("value", 10)
        self.spin_colormap.setObjectName("spin_colormap")
        self.verticalLayout_4.addWidget(self.spin_colormap)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.comb_colormap_style = ColormapChoser()
        self.verticalLayout_4.addWidget(self.comb_colormap_style)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_variable = QtWidgets.QComboBox(Form)
        self.comboBox_variable.setObjectName("comboBox_variable")
        self.verticalLayout_2.addWidget(self.comboBox_variable)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.list_zone_surface = QtWidgets.QColumnView(Form)
        self.list_zone_surface.setObjectName("list_zone_surface")
        self.verticalLayout_2.addWidget(self.list_zone_surface)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout_entirety.addLayout(self.horizontalLayout_4)

        # 第三行
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        # 双滑块进度条
        self.colorprogress_layout = QtWidgets.QHBoxLayout()
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.colorprogress_layout.addWidget(self.checkBox_3)
        self.range_slider = QLabeledRangeSlider()
        self.range_slider.setOrientation(Qt.Horizontal)
        self.range_slider.setMinimum(0)
        self.range_slider.setMaximum(10)
        self.range_slider.setValue([0, 10])
        self.colorprogress_layout.addWidget(self.range_slider)
        self.verticalLayout.addLayout(self.colorprogress_layout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_entirety.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_entirety.addLayout(self.horizontalLayout_5)
        self.verticalLayout_entirety.setStretch(0, 1)
        self.verticalLayout_entirety.setStretch(1, 6)
        self.verticalLayout_entirety.setStretch(2, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Contour"))
        self.le_name.setText(_translate("Form", "绘图名"))
        self.groupBox_2.setTitle(_translate("Form", "绘图选项"))
        self.checkBox_grid.setText(_translate("Form", "显示网格"))
        self.checkBox_smooth.setText(_translate("Form", "平滑"))
        self.groupBox_3.setTitle(_translate("Form", "Colormap"))
        self.checkBox_log.setText(_translate("Form", "取log值"))
        self.label_6.setText(_translate("Form", "分段数"))
        self.label_7.setText(_translate("Form", "风格"))
        self.label_3.setText(_translate("Form", "变量"))
        self.label_5.setText(_translate("Form", "Zone"))
        self.groupBox.setTitle(_translate("Form", "等值面"))
        self.checkBox_2.setText(_translate("Form", "指定等值面数量"))
        self.checkBox_3.setText(_translate("Form", "颜色条范围"))
        self.label_2.setText(_translate("Form", "等值面算法"))
        self.comboBox.setItemText(0, _translate("Form", "contour"))
        self.comboBox.setItemText(1, _translate("Form", "marching_cubes"))
        self.comboBox.setItemText(2, _translate("Form", "flying_edges"))
        self.label_4.setText(_translate("Form", "透明度"))
        self.pushButton.setText(_translate("Form", "绘制"))
        self.pushButton_2.setText(_translate("Form", "取消"))

    def displayAction(self):
        # print("disp")
        data = {
            "name": self.text_plot_name.text(),
            "style": self.comboBox_style.currentText(),
            "mesh": self.checkBox_grid.isChecked(),
            "smooth": self.checkBox_smooth.isChecked(),
            "log_scale": self.checkBox_log.isChecked(),
            "colormap": self.comb_colormap_style.currentText(),
            "colormapsize": self.spin_colormap.value(),

            "varName": self.comboBox_variable.currentText(),
            "zoneName": [item.data() for item in self.list_zone_surface.selectedIndexes()],

            "specify_iso": self.checkBox_2.isChecked(),
            "iso_numbers": self.spinBox.value(),
            "specify_range": self.checkBox_3.isChecked(),
            "iso_range": (self.range_slider.value()),
            "screening_tech": self.comboBox.currentText(),
            "opacity": self.doubleSpinBox.value(),
                }
        self.draw_handler(data)


class VolumePlotOptionDialog(QDialog):
    def __init__(self, varNames=[], zoneNames=[], call_back_draw=None, parent=None):
        super(VolumePlotOptionDialog, self).__init__(parent)
        # self.setMinimumSize(500, 450)
        # self.setMaximumSize(700, 650)
        # self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowIcon(QIcon(':/png/icon/volume_option.png'))
        self.setupUi(self)

        # data init
        self.comboBox_style.addItems(["surface", "points", "wireframe"])

        self.zoneNames = zoneNames
        self.comboBox_variable.addItems(varNames)
        qlm = QStringListModel(zoneNames)
        self.list_zone_surface.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_zone_surface.setModel(qlm)
        self.list_zone_surface.setCurrentIndex(qlm.index(0, 0))

        # draw call back function
        self.draw_handler = call_back_draw

        self.init_widget()

    def init_widget(self):
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.valueChanged.connect(lambda: self.label_2.setText(str(self.horizontalSlider.value()/1000)))
        self.pushButton.clicked.connect(self.displayAction)

    def displayAction(self):
        data = {
            "name": self.text_plot_name.text(),
            "style": self.comboBox_style.currentText(),
            "mesh": self.checkBox_grid.isChecked(),
            "smooth": self.checkBox_smooth.isChecked(),
            "log_scale": self.checkBox_log.isChecked(),
            "colormap": self.comb_colormap_style.currentText(),
            "colormapsize": self.spin_colormap.value(),

            "varName": self.comboBox_variable.currentText(),
            "zoneName": [item.data() for item in self.list_zone_surface.selectedIndexes()],

            "voxel_size": self.horizontalSlider.value()/1000,
            "opacity": self.doubleSpinBox.value(),
                }
        self.draw_handler(data)

    def setupUi(self, volume_window):
        volume_window.setObjectName("volume_window")
        volume_window.resize(550, 600)

        self.verticalLayout_entirety = QtWidgets.QVBoxLayout(volume_window)
        self.verticalLayout_entirety.setObjectName("verticalLayout_entirety")

        # 第一行
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_name = QtWidgets.QLabel(volume_window)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        self.text_plot_name = QtWidgets.QLineEdit(volume_window)
        self.text_plot_name.setObjectName("text_plot_name")
        self.horizontalLayout.addWidget(self.text_plot_name)
        self.verticalLayout_entirety.addLayout(self.horizontalLayout)

        # 第二行
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(volume_window)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_style = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_style.setObjectName("comboBox_style")
        self.verticalLayout_3.addWidget(self.comboBox_style)
        self.checkBox_grid = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_grid.setObjectName("checkBox_grid")
        self.verticalLayout_3.addWidget(self.checkBox_grid)
        self.checkBox_smooth = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_smooth.setObjectName("checkBox_smooth")
        self.verticalLayout_3.addWidget(self.checkBox_smooth)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(volume_window)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_log = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_log.setObjectName("checkBox_log")
        self.verticalLayout_4.addWidget(self.checkBox_log)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.spin_colormap = QtWidgets.QSpinBox(self.groupBox_3)
        self.spin_colormap.setProperty("value", 10)
        self.spin_colormap.setObjectName("spin_colormap")
        self.verticalLayout_4.addWidget(self.spin_colormap)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.comb_colormap_style = ColormapChoser()
        self.verticalLayout_4.addWidget(self.comb_colormap_style)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(volume_window)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_variable = QtWidgets.QComboBox(volume_window)
        self.comboBox_variable.setObjectName("comboBox_variable")
        self.verticalLayout_2.addWidget(self.comboBox_variable)
        self.label_5 = QtWidgets.QLabel(volume_window)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.list_zone_surface = QtWidgets.QColumnView(volume_window)
        self.list_zone_surface.setObjectName("list_zone_surface")
        self.verticalLayout_2.addWidget(self.list_zone_surface)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout_entirety.addLayout(self.horizontalLayout_4)

        # 第三行
        self.Voxel_GroupBox = QtWidgets.QGroupBox(volume_window)
        self.Voxel_GroupBox.setObjectName("Voxel_GroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Voxel_GroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vsize_horizontalLayout = QtWidgets.QHBoxLayout()
        self.vsize_horizontalLayout.setObjectName("vsize_horizontalLayout")
        self.label = QtWidgets.QLabel(self.Voxel_GroupBox)
        self.label.setObjectName("label")
        self.vsize_horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.Voxel_GroupBox)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.vsize_horizontalLayout.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.Voxel_GroupBox)
        self.label_2.setObjectName("label_2")
        self.vsize_horizontalLayout.addWidget(self.label_2)
        self.vsize_horizontalLayout.setStretch(0, 2)
        self.vsize_horizontalLayout.setStretch(1, 7)
        self.vsize_horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.vsize_horizontalLayout)
        self.horizontalLayout_opacity = QtWidgets.QHBoxLayout()
        self.horizontalLayout_opacity.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_opacity.setSpacing(7)
        self.horizontalLayout_opacity.setObjectName("horizontalLayout_opacity")
        self.label_4 = QtWidgets.QLabel(self.Voxel_GroupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_opacity.addWidget(self.label_4)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.Voxel_GroupBox)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_opacity.addWidget(self.doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_opacity)
        self.verticalLayout_entirety.addWidget(self.Voxel_GroupBox)
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
        self.verticalLayout_entirety.addLayout(self.horizontalLayout_5)
        self.verticalLayout_entirety.setStretch(0, 1)
        self.verticalLayout_entirety.setStretch(1, 6)
        self.verticalLayout_entirety.setStretch(2, 2)

        self.retranslateUi(volume_window)
        QtCore.QMetaObject.connectSlotsByName(volume_window)

    def retranslateUi(self, volume_window):
        _translate = QtCore.QCoreApplication.translate
        volume_window.setWindowTitle(_translate("volume_window", "Volume"))

        self.le_name.setText(_translate("Form", "绘图名"))
        self.groupBox_2.setTitle(_translate("Form", "绘图选项"))
        self.checkBox_grid.setText(_translate("Form", "显示网格"))
        self.checkBox_smooth.setText(_translate("Form", "平滑"))
        self.groupBox_3.setTitle(_translate("Form", "Colormap"))
        self.checkBox_log.setText(_translate("Form", "取log值"))
        self.label_6.setText(_translate("Form", "分段数"))
        self.label_7.setText(_translate("Form", "风格"))
        self.label_3.setText(_translate("Form", "变量"))
        self.label_5.setText(_translate("Form", "Zone"))

        self.Voxel_GroupBox.setTitle(_translate("volume_window", "Volume Rendering"))
        self.label.setText(_translate("volume_window", "不透明度单位距离"))
        self.label_2.setText(_translate("volume_window", "0.1"))
        self.label_4.setText(_translate("volume_window", "透明度"))
        self.pushButton.setText(_translate("volume_window", "绘制"))
        self.pushButton_2.setText(_translate("volume_window", "取消"))


class SlicePlotOptionDialog(QDialog):
    def __init__(self, varNames=[], zoneNames=[], call_back_draw=None, parent=None):
        super(SlicePlotOptionDialog, self).__init__(parent)
        # self.setMinimumSize(500, 450)
        # self.setMaximumSize(700, 650)
        # self.resize(550, 500)
        self.sliceOption_group = None
        self.slice_type = None
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowIcon(QIcon(':/png/icon/slice_option.png'))
        self.setupUi(self)

        # data init
        self.comboBox_style.addItems(["surface", "points", "wireframe"])

        self.zoneNames = zoneNames
        self.comboBox_variable.addItems(varNames)
        qlm = QStringListModel(zoneNames)
        self.list_zone_surface.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_zone_surface.setModel(qlm)
        self.list_zone_surface.setCurrentIndex(qlm.index(0, 0))

        # draw call back function
        self.draw_handler = call_back_draw

        self.init_widget()

    def init_widget(self):
        self.pushButton.clicked.connect(self.displayAction)

        self.sliceOption_group = QButtonGroup(self)
        self.sliceOption_group.addButton(self.radioButton_ortho)
        self.sliceOption_group.addButton(self.radioButton_origin)
        self.sliceOption_group.addButton(self.radioButton_along)
        self.sliceOption_group.addButton(self.radioButton_mesh)
        self.radioButton_mesh.setChecked(True)

        doubleValidator = QDoubleValidator()
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(4)
        self.lineEdit_origin_x.setValidator(doubleValidator)
        self.lineEdit_origin_y.setValidator(doubleValidator)
        self.lineEdit_origin_z.setValidator(doubleValidator)

    def displayAction(self):
        data = {
            "name": self.text_plot_name.text(),
            "style": self.comboBox_style.currentText(),
            "mesh": self.checkBox_grid.isChecked(),
            "smooth": self.checkBox_smooth.isChecked(),
            "log_scale": self.checkBox_log.isChecked(),
            "colormap": self.comb_colormap_style.currentText(),
            "colormapsize": self.spin_colormap.value(),

            "varName": self.comboBox_variable.currentText(),
            "zoneName": [item.data() for item in self.list_zone_surface.selectedIndexes()],

            "opacity": self.SpinBox_opacity.value()
                }

        # 切片类型
        if self.sliceOption_group.checkedButton() == self.radioButton_ortho:
            self.slice_type = "orthogonality"
        elif self.sliceOption_group.checkedButton() == self.radioButton_origin:
            self.slice_type = "origin_specified"
        elif self.sliceOption_group.checkedButton() == self.radioButton_along:
            self.slice_type = "along_axis"
        elif self.sliceOption_group.checkedButton() == self.radioButton_mesh:
            self.slice_type = "mesh"
        data['sliceType'] = self.slice_type

        # 切片参数
        if self.slice_type == "origin_specified":
            origin = [self.lineEdit_origin_x.text(), self.lineEdit_origin_y.text(), self.lineEdit_origin_z.text()]
            normal = [self.comboBox_normal_x.currentText(), self.comboBox_normal_y.currentText(), self.comboBox_normal_z.currentText()]
            data['origin'] = list(map(float, origin))
            data['normal'] = list(map(int, normal))
        if self.slice_type == "along_axis":
            if self.comboBox_axis.currentText() == 'X轴':
                data['axis'] = 'x'
            elif self.comboBox_axis.currentText() == 'Y轴':
                data['axis'] = 'y'
            elif self.comboBox_axis.currentText() == 'Z轴':
                data['axis'] = 'z'
            data['slice_num'] = self.spinBox_sliceNum.value()

        self.draw_handler(data)

    def setupUi(self, slice_window):
        slice_window.setObjectName("slice_window")
        slice_window.resize(550, 855)

        # 第一行
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(slice_window)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_row_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_row_1.setObjectName("horizontalLayout_row_1")
        self.label_le_name = QtWidgets.QLabel(slice_window)
        self.label_le_name.setObjectName("label_le_name")
        self.horizontalLayout_row_1.addWidget(self.label_le_name)
        self.text_plot_name = QtWidgets.QLineEdit(slice_window)
        self.text_plot_name.setObjectName("text_plot_name")
        self.horizontalLayout_row_1.addWidget(self.text_plot_name)
        self.verticalLayout_6.addLayout(self.horizontalLayout_row_1)

        # 第二行
        self.horizontalLayout_row_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_row_2.setObjectName("horizontalLayout_row_2")

        # 第二行第一列
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(slice_window)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_style = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_style.setObjectName("comboBox_style")
        self.verticalLayout_3.addWidget(self.comboBox_style)
        self.checkBox_grid = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_grid.setObjectName("checkBox_grid")
        self.verticalLayout_3.addWidget(self.checkBox_grid)
        self.checkBox_smooth = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_smooth.setObjectName("checkBox_smooth")
        self.verticalLayout_3.addWidget(self.checkBox_smooth)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(slice_window)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_log = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_log.setObjectName("checkBox_log")
        self.verticalLayout_4.addWidget(self.checkBox_log)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.spin_colormap = QtWidgets.QSpinBox(self.groupBox_3)
        self.spin_colormap.setProperty("value", 10)
        self.spin_colormap.setObjectName("spin_colormap")
        self.verticalLayout_4.addWidget(self.spin_colormap)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.comb_colormap_style = ColormapChoser()
        self.verticalLayout_4.addWidget(self.comb_colormap_style)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_row_2.addLayout(self.verticalLayout_5)

        # 第二行第二列
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(slice_window)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.comboBox_variable = QtWidgets.QComboBox(slice_window)
        self.comboBox_variable.setObjectName("comboBox_variable")
        self.verticalLayout_2.addWidget(self.comboBox_variable)
        self.label_16 = QtWidgets.QLabel(slice_window)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.list_zone_surface = QtWidgets.QColumnView(slice_window)
        self.list_zone_surface.setObjectName("list_zone_surface")
        self.verticalLayout_2.addWidget(self.list_zone_surface)
        self.horizontalLayout_row_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_row_2.setStretch(0, 6)
        self.horizontalLayout_row_2.setStretch(1, 5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_row_2)

        # 第三行
        self.Slice_GroupBox = QtWidgets.QGroupBox(slice_window)
        self.Slice_GroupBox.setObjectName("Slice_GroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Slice_GroupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.radioButton_mesh = QtWidgets.QRadioButton(self.Slice_GroupBox)
        self.radioButton_mesh.setObjectName("radioButton_mesh")
        self.verticalLayout.addWidget(self.radioButton_mesh)
        self.radioButton_ortho = QtWidgets.QRadioButton(self.Slice_GroupBox)
        self.radioButton_ortho.setObjectName("radioButton_ortho")
        self.verticalLayout.addWidget(self.radioButton_ortho)
        self.radioButton_origin = QtWidgets.QRadioButton(self.Slice_GroupBox)
        self.radioButton_origin.setObjectName("radioButton_origin")
        self.verticalLayout.addWidget(self.radioButton_origin)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.Slice_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_origin_x = QtWidgets.QLineEdit(self.Slice_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_origin_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_origin_x.setSizePolicy(sizePolicy)
        self.lineEdit_origin_x.setObjectName("lineEdit_origin_x")
        self.horizontalLayout.addWidget(self.lineEdit_origin_x)
        self.label_3 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_origin_y = QtWidgets.QLineEdit(self.Slice_GroupBox)
        self.lineEdit_origin_y.setObjectName("lineEdit_origin_y")
        self.horizontalLayout.addWidget(self.lineEdit_origin_y)
        self.label_5 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_origin_z = QtWidgets.QLineEdit(self.Slice_GroupBox)
        self.lineEdit_origin_z.setObjectName("lineEdit_origin_z")
        self.horizontalLayout.addWidget(self.lineEdit_origin_z)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(self.Slice_GroupBox)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        # self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBox_normal_x = QtWidgets.QComboBox(self.Slice_GroupBox)
        self.comboBox_normal_x.addItems(["0", "1"])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_normal_x.sizePolicy().hasHeightForWidth())
        self.comboBox_normal_x.setSizePolicy(sizePolicy)
        self.comboBox_normal_x.setObjectName("comboBox_normal_x")
        self.horizontalLayout_2.addWidget(self.comboBox_normal_x)
        self.label_8 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.comboBox_normal_y = QtWidgets.QComboBox(self.Slice_GroupBox)
        self.comboBox_normal_y.addItems(["0", "1"])
        self.comboBox_normal_y.setObjectName("comboBox_normal_y")
        self.comboBox_normal_y.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.comboBox_normal_y)
        self.label_9 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.comboBox_normal_z = QtWidgets.QComboBox(self.Slice_GroupBox)
        self.comboBox_normal_z.addItems(["0", "1"])
        self.comboBox_normal_z.setObjectName("comboBox_normal_z")
        self.horizontalLayout_2.addWidget(self.comboBox_normal_z)
        self.comboBox_normal_z.setSizePolicy(sizePolicy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.radioButton_along = QtWidgets.QRadioButton(self.Slice_GroupBox)
        self.radioButton_along.setObjectName("radioButton_along")
        self.verticalLayout.addWidget(self.radioButton_along)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_10 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.comboBox_axis = QtWidgets.QComboBox(self.Slice_GroupBox)
        self.comboBox_axis.setObjectName("comboBox_axis")
        self.comboBox_axis.addItem("")
        self.comboBox_axis.addItem("")
        self.comboBox_axis.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_axis)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_11 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBox_sliceNum = QtWidgets.QSpinBox(self.Slice_GroupBox)
        self.spinBox_sliceNum.setObjectName("spinBox_sliceNum")
        self.horizontalLayout_4.addWidget(self.spinBox_sliceNum)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_opacity = QtWidgets.QHBoxLayout()
        self.horizontalLayout_opacity.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_opacity.setSpacing(7)
        self.horizontalLayout_opacity.setObjectName("horizontalLayout_opacity")
        self.label_4 = QtWidgets.QLabel(self.Slice_GroupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_opacity.addWidget(self.label_4)
        self.SpinBox_opacity = QtWidgets.QDoubleSpinBox(self.Slice_GroupBox)
        self.SpinBox_opacity.setMaximum(1.0)
        self.SpinBox_opacity.setSingleStep(0.1)
        self.SpinBox_opacity.setProperty("value", 0.5)
        self.SpinBox_opacity.setObjectName("SpinBox_opacity")
        self.horizontalLayout_opacity.addWidget(self.SpinBox_opacity)
        self.verticalLayout.addLayout(self.horizontalLayout_opacity)
        self.verticalLayout_6.addWidget(self.Slice_GroupBox)

        # 第四行
        self.horizontalLayout_row_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_row_4.setObjectName("horizontalLayout_row_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_row_4.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(slice_window)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_row_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(slice_window)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_row_4.addWidget(self.pushButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_row_4.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_row_4)
        self.verticalLayout_6.setStretch(1, 5)
        self.verticalLayout_6.setStretch(2, 4)

        self.retranslateUi(slice_window)
        QtCore.QMetaObject.connectSlotsByName(slice_window)

    def retranslateUi(self, slice_window):
        _translate = QtCore.QCoreApplication.translate
        slice_window.setWindowTitle(_translate("slice_window", "Slice"))
        self.label_le_name.setText(_translate("slice_window", "绘图名"))
        self.groupBox_2.setTitle(_translate("slice_window", "绘图选项"))
        self.checkBox_grid.setText(_translate("slice_window", "显示网格"))
        self.checkBox_smooth.setText(_translate("slice_window", "平滑"))
        self.groupBox_3.setTitle(_translate("slice_window", "Colormap"))
        self.checkBox_log.setText(_translate("slice_window", "取log值"))
        self.label_13.setText(_translate("slice_window", "分段数"))
        self.label_14.setText(_translate("slice_window", "风格"))
        self.label_15.setText(_translate("slice_window", "变量"))
        self.label_16.setText(_translate("slice_window", "Zone"))
        self.Slice_GroupBox.setTitle(_translate("slice_window", "Slicing"))
        self.radioButton_mesh.setText(_translate("slice_window", "不切片"))
        self.radioButton_ortho.setText(_translate("slice_window", "正交切片"))
        self.radioButton_origin.setText(_translate("slice_window", "指定位置切片"))
        self.label.setText(_translate("slice_window", "原点"))
        self.label_2.setText(_translate("slice_window", "x"))
        self.label_3.setText(_translate("slice_window", "y"))
        self.label_5.setText(_translate("slice_window", "z"))
        self.label_6.setText(_translate("slice_window", "法向量方向"))
        self.label_7.setText(_translate("slice_window", "x"))
        self.label_8.setText(_translate("slice_window", "y"))
        self.label_9.setText(_translate("slice_window", "z"))
        self.radioButton_along.setText(_translate("slice_window", "沿轴切片"))
        self.label_10.setText(_translate("slice_window", "轴向"))
        self.comboBox_axis.setItemText(0, _translate("slice_window", "X轴"))
        self.comboBox_axis.setItemText(1, _translate("slice_window", "Y轴"))
        self.comboBox_axis.setItemText(2, _translate("slice_window", "Z轴"))
        self.label_11.setText(_translate("slice_window", "切片数量"))
        self.label_4.setText(_translate("slice_window", "透明度"))
        self.pushButton.setText(_translate("slice_window", "绘制"))
        self.pushButton_2.setText(_translate("slice_window", "取消"))


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
