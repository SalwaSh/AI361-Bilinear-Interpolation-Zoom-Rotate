"""
Student Name: Salwa Shama
Student Number: 4010405
UPM Email: 4010405@upm.edu.sa
OS: Windows 11
Python 3.10.9

This is a small program provides two functionalities: zooming and rotation, using bilinear interpolation on grayscale images.
"""
# import built-in libraries/modules.
from skimage import io
import numpy as np
import os
# import the module that includes two main functions: zoom_image and rotate_image.
from image_utils import zoom_image, rotate_image

print("Hi there 👋!, Welcome to My Interpolation Program")
print("""This program offers two main functionalities for manipulating images:
        1. Zoom: You can zoom in or out of an image to adjust its size.
        2. Rotate: You can rotate an image by giving an angle in degrees""")

selected_operation = input("\nStep 1 out of 3: Please, enter the operation number you want to apply from the list above: ")
original_image_path = input("Step 2 out of 3: Please, provide the path to the desired image to be modified: ")
original_image = io.imread(original_image_path, as_gray=True)

if selected_operation == "1":
    zoom_factor = float(input("Step 3 out of 3: Please, enter the zoom factor: (NOTE: A factor > 1 enlarges the image, while a factor < 1 shrinks it.) "))
    print("\nPlease wait, as this process may take a while... ⏳")
    zoomed_image = zoom_image(original_image, zoom_factor)
    output_image = zoomed_image.astype(np.uint8)


elif selected_operation == "2":
    rotation_angle = -float(input("Step 3:Enter the angle of rotation: (NOTE: The angle of rotation should be specified in degrees.) "))
    print("\nPlease wait, as this process may take a while... ⏳")
    rotated_image = rotate_image(original_image, rotation_angle)
    output_image = rotated_image.astype(np.uint8)

else:
    print("Please, enter a correct option.")

# save the modified image.
modified_image_path = "output_image.jpg"
io.imsave(modified_image_path, output_image)
print("The process has been completed ✅.")
print("Saved image path:", os.path.abspath(modified_image_path))


