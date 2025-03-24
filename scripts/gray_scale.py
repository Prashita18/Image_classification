

import os
from PIL import Image

# This script converts images in the input folder to grayscale and saves them in the output folder.  
# It handles image format issues, ensures compatibility, and logs any failed conversions.

input_folder = r"C:\Users\Prashita\OneDrive\Desktop\Assignment\Chimney"
output_folder = r"C:\Users\Prashita\OneDrive\Desktop\Assignment\Images\Chimney"

os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

processed_count = 0
failed_images = []

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB")  # Fix RGBA, CMYK, or P mode issues
            img = img.convert("L")  # Convert to grayscale
            img.save(output_path)
            processed_count += 1
    except Exception as e:
        print(f"Skipping {filename}: {e}")
        failed_images.append(filename)

print(f"Processed {processed_count} images successfully.")
print(f"Skipped {len(failed_images)} images. Check logs.")
