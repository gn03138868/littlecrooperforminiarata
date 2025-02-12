# These codes are adjusted for hourly hinoki analysis in Kiryu for observing root tips 
# (It is not easy to obtain 200X200 pixels images one by one. So I wrote a simple script for doing it when images over 100.)

# pip install pillow
# in cmd

import os
from PIL import Image

# Directory containing your input images
input_directory = 'E:/Shitephen/plot5-hourly/20200814-sunny-original' 
## rewrite in your own path

# Directory where you want to save the cropped images
output_directory = 'E:/Shitephen/plot5-hourly/20200814-sunny' 
## rewrite in your own path

# Define the edge dimensions to be cropped
left, top, right, bottom = 2430, 5270, 2470, 1550
# our images are in A4 size (5100X7020 pixel^2), you can adjust on your own size to crop 200X200 pixel^2 images

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Loop through each image in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust file extensions as needed
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Load the image
        image = Image.open(input_path)

        # Crop the edges
        cropped_image = image.crop((left, top, image.width - right, image.height - bottom))

        # Save the cropped image to the output directory
        cropped_image.save(output_path)

        print(f"Cropped and saved: {output_path}")

print("All images processed.")
