import csv
import os

# This script generates a CSV file listing image filenames and their corresponding class labels.  
# It scans through subfolders in the dataset directory, treating each folder name as a class label.

csv_file = "dataset_labels.csv"
dataset_path = r"C:\Users\Prashita\OneDrive\Desktop\Assignment\Images"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["filename", "label"])  # Header

    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)

        if os.path.isdir(class_path):
            for image in sorted(os.listdir(class_path)):  # Ensure only image files
                if image.endswith(('.jpg', '.png', '.jpeg')):
                    writer.writerow([image, class_name])  # Write filename and label

print(f"CSV file created: {csv_file}")
