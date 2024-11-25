import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d
import laspy


#matplotlib.use('TkAgg')


def single_visualize():

    
    image_path = r"/home/ahad/Desktop/research/PointCloud-Diffusion/data/img"
    lidar_path = r"/home/ahad/Desktop/research/PointCloud-Diffusion/data/velo"

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

    #select 1000 random points from lidar data
    lidar_data = lidar_data[np.random.choice(lidar_data.shape[0], 1000, replace=False), :]


    x, y, z = lidar_data[:, 0], lidar_data[:, 1], lidar_data[:, 2]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', s=5)  


    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Point Cloud Visualization")

    plt.show()




def ply_las_convert(path=None):
    # Path to the folder containing PLY files
    lidar_path = r"/home/ahad/Downloads/data_3d_semantics_test/data_3d_semantics/test/2013_05_28_drive_0008_sync/static"
    lidar_files = sorted(glob.glob(f"{lidar_path}/*.ply"))

    if not lidar_files:
        print("No PLY files found in the specified directory.")
        return

    lidar_file = lidar_files[0]  # Process the first file (or modify to loop through all files)

    # Load the PLY file
    pcd = o3d.io.read_point_cloud(lidar_file)

    # Convert point cloud data to NumPy array
    points = np.asarray(pcd.points)

    # Create a header for the LAS file
    header = laspy.LasHeader(point_format=3, version="1.2")

    # Create a LasData object and populate point data
    las_data = laspy.LasData(header)
    las_data.x = points[:, 0]
    las_data.y = points[:, 1]
    las_data.z = points[:, 2]

    # Save as LAS
    output_file = "output1.las"
    with laspy.open(output_file, mode="w", header=header) as writer:
        writer.write_points(las_data)

    print(f"Converted {lidar_file} to {output_file}")

# Call the function
ply_las_convert()



    
if __name__ == "__main__":
    #single_visualize()
    ply_las_convert()


    
    


