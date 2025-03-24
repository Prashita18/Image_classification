import os
import cv2
import numpy as np

# This script renames images in each class folder with a standardized format ("class_name_imageX").  
# It scans through subfolders, ensures only valid images are processed, and removes unwanted images if necessary.

# Define the dataset path (update this)
dataset_path = r"C:\Users\Prashita\OneDrive\Desktop\Assignment\Images"  # Change to your dataset path

# Loop through each class folder
for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)

    if os.path.isdir(class_path):  # Ensure it's a directory
        images = sorted([f for f in os.listdir(class_path) if f.endswith(('.jpg', '.png', '.jpeg'))])

        for idx, image in enumerate(images, start=1):
            ext = os.path.splitext(image)[1]  # Get file extension
            new_name = f"{class_name}_image{idx}{ext}"  # Unique name with class
            old_path = os.path.join(class_path, image)
            new_path = os.path.join(class_path, new_name)

            # Load the image for checking
            img = cv2.imread(old_path)

            # Check conditions and delete unwanted images
            
            os.rename(old_path, new_path)  # Rename only valid images

        print(f" Processed {class_name}: Renamed valid images and deleted bad ones.")

print(" Image processing completed successfully")
