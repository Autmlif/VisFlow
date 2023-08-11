import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from Resource import images_rc
import matplotlib as mpl
mpl.use("Qt5Agg")
import numpy as np

# 流场基本绘制的对话框
#

class MeshDataPlotOptionDialog(QDialog):
    pass

class VolumePlotOptionDialog(QDialog):
    pass

class ContoursOptionDialog(QDialog):
    def __init__(self, varNames=[], zoneNames=[], call_back_draw=None, parent=None):
        super(ContoursOptionDialog, self).__init__(parent)
        self.setMinimumSize(500, 450)
        self.setMaximumSize(700, 650)
        self.resize(550, 500)
        self.absolute_path = os.path.split(sys.argv[0])[0]
        self.setWindowTitle('绘制选项')
        self.setWindowIcon(QIcon(':/png/icon/contour_option.png'))
        self._layout_init()

        # data init
        self.zoneNames = zoneNames
        self.comb_varible.addItems(varNames)
        qlm = QStringListModel(zoneNames)
        self.list_zone_surface.setModel(qlm)
        self.list_zone_surface.setCurrentIndex(qlm.index(0,0))
        # draw call back function
        self.draw_handler = call_back_draw

        # event define
        self.btn_display.clicked.connect(self.displayAction)


    def displayAction(self):
        # print("disp")
        data ={"name":self.le_name.text(),
               "style":self.comb_style.currentText(),
               "mesh":self.check_mesh.isChecked(),
               "smooth":self.check_smooth.isChecked(),
               "log_scale":self.check_logScale.isChecked(),
               "colormap":self.comb_colormap_style.currentText(),
               "colormapsize":self.spin_colormap_size.value(),
               "varName":self.comb_varible.currentText(),
               "zoneName":[item.data() for item in self.list_zone_surface.selectedIndexes()]
               }
        self.draw_handler(data)

    def _layout_init(self):
        # 纵向布局
        layout_out = QVBoxLayout()
        layout_out.setContentsMargins(20, 10, 20, 10)
        layout_out.setSpacing(10)
        #第一行
        layout_row1 = QHBoxLayout()
        layout_row1.addWidget(QLabel("绘图名"))
        self.le_name = QLineEdit(self)
        layout_row1.addWidget(self.le_name)
        layout_out.addLayout(layout_row1)

        #第二行
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
        self.comb_style.addItems(["surface","points","wireframe"]) # ``style='surface'``, ``style='wireframe'``, ``style='points'``, ``style='points_gaussian'``
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

        #第三行
        layout_row3 = QHBoxLayout()
        self.btn_display = QPushButton("绘制")
        self.btn_cancel = QPushButton("取消")
        layout_row3.addStretch()
        layout_row3.addWidget(self.btn_display)
        layout_row3.addWidget(self.btn_cancel)
        layout_row3.addStretch()
        layout_row3.setSpacing(20)
        layout_out.addLayout(layout_row3)
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

    #返回当前选择
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
    cDemo = ContoursOptionDialog(varNames=["a", "b", "c"], zoneNames=["aaa", "bbb"], call_back_draw=fun)
    cDemo.show()
    sys.exit(app.exec_())