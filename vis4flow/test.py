import pyvista as pv
import numpy as np
## 生成一组点云的坐标，然后构建点云的mesh
points = np.random.rand(30000, 3)
point_cloud = pv.PolyData(points)
# 画点云
point_cloud.plot(eye_dome_lighting=True)

data = points[:,-1]
point_cloud["value"] = data

def compute_vectors(mesh):
    origin = mesh.center
    vectors = mesh.points - origin
    vectors = vectors / np.linalg.norm(vectors, axis=1)[:, None]
    return vectors

vectors = compute_vectors(point_cloud)
point_cloud['vectors'] = vectors
arrows = point_cloud.glyph(orient='vectors', scale=False, factor=0.15,) #通过这个函数构建箭头
# Display the arrows
plotter = pv.Plotter()
# plotter.add_mesh(point_cloud, color='maroon', point_size=10.,
#                  render_points_as_spheres=True)
# plotter.add_mesh(arrows, color='lightblue')
# plotter.add_point_labels([point_cloud.center,], ['Center',],
#                          point_color='yellow', point_size=20)
plotter.show_grid()
plotter.show()