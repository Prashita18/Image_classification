import Augmentor
from PIL import Image
import os

# This script applies data augmentation to images in the input folder using Augmentor.  
# It performs rotations, flips, brightness/contrast adjustments, and zooming.  
# It also ensures all images are in RGB format before augmentation to avoid compatibility issues.

# Define paths
input_folder = r"C:\Users\Prashita\OneDrive\Desktop\Assignment\Land"  # Change for each class
output_folder = "Augmentation"
os.makedirs(output_folder, exist_ok=True)

# Initialize Augmentor pipeline
p = Augmentor.Pipeline(input_folder, output_directory=output_folder)

# Add augmentations
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.flip_left_right(probability=0.5)
p.random_brightness(probability=0.5, min_factor=0.7, max_factor=1.3)
p.random_contrast(probability=0.5, min_factor=0.7, max_factor=1.3)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)

# Convert images to RGB to avoid RGBA issues
def convert_images_to_rgb(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                if img.mode in ("RGBA", "P"):  # Convert to RGB
                    img = img.convert("RGB")
                    img.save(filepath)  # Overwrite with RGB image
        except Exception as e:
            print(f"Skipping {filename}: {e}")

convert_images_to_rgb(input_folder)  # Fix images before augmentation

# Generate augmented images (Target: 1000 per class)
num_samples = 1000
p.sample(num_samples)

print(f"Augmented images saved in {output_folder}")
