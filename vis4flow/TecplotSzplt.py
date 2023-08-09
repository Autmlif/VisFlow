import pyvista
from UI.File.Vis4Flow import pytecio
import numpy as np
from pyvista import CellType
#
# 解析Tecplot文件，组织成pyvist可绘制的格式。即UnstructuredGrid。
# 根据文件，FEBRICK对应到的CellType是HEXAHEDRON，即六面体，由8个点组成。如果是其它CellType的数据，则需对本文件进行修改。
#
class TecplotDataVis:
    def __init__(self, szlp_dat):
        self.szlp_dat = szlp_dat
        self.zones = {}
    #数据中，至少包含一个zone,不同的zone有不同的名字，具体有些什么名字，由文件中给出
    def getZoneNames(self):
        return self.szlp_dat.nameZones
    #数据中，每一个zone，数据，应有不同的流场变量，比如密度、温度、速度等，具体由文件中内容决定
    def getVarNames(self):
        return self.szlp_dat.nameVars[3:]

    #按名字，给出zone数据
    def getZoneVista(self, zoneName):
        if zoneName in self.zones.keys():
            grid = self.zones.get(zoneName)
        else:
            zone = self.szlp_dat.get(zoneName)
            points = np.column_stack((zone['X'],zone['Y'],zone['Z']))
            ele_num = len(zone.Elements)
            cells = np.insert(zone.Elements - 1, 0, np.ones(ele_num) * 8, axis=1).ravel()
            celltypes = np.full(ele_num, CellType.HEXAHEDRON, dtype=np.uint8)
            grid = pyvista.UnstructuredGrid(cells, celltypes, points)
            for varName in self.szlp_dat.nameVars[3:]:
                grid.cell_data[varName] = zone[varName]
            self.zones[zoneName] = grid
        return grid


def read(filename) -> TecplotDataVis:
    szlp_dat = pytecio.read(filename, False)
    return TecplotDataVis(szlp_dat)

