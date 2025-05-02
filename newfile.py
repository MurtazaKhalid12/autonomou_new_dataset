import os

image_folder = r'C:\Users\PMLS\Videos\simulator-windows-64\IMG'
image_extensions = ('.jpg', '.jpeg', '.png')

num_images = len([f for f in os.listdir(image_folder) if f.lower().endswith(image_extensions)])
print(f"Number of images in {image_folder}: {num_images}")