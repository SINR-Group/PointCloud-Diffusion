import glob
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


image_path = r"C:\Users\JANAB\Desktop\Research\3D_Reconstruction\KITTI_Dataset\image_00\data"
lidar_path = r"C:\Users\JANAB\Desktop\Research\3D_Reconstruction\KITTI_Dataset\velodyne_points\data"

image_files = sorted(glob.glob(f"{image_path}/*.png"))
lidar_files = sorted(glob.glob(f"{lidar_path}/*.bin"))

image_file = image_files[0]
lidar_file = lidar_files[0]

print(f"Loading LIDAR file: {lidar_file}")
print(f"Loading IMAGE file: {image_file}")

try:
    lidar_data = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)
    print(f"Lidar data shape: {lidar_data.shape}")
except Exception as e:
    print(f"Error loading LIDAR file: {e}")
    exit()

if lidar_data.shape[0] == 0:
    print("LIDAR data is empty. Please check the .bin file.")
    exit()


lidar_data = lidar_data[:10000]
x, y, z = lidar_data[:, 0], lidar_data[:, 1], lidar_data[:, 2]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', s=5)  


ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Point Cloud Visualization")

plt.show()
