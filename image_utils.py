import numpy as np
import math

"""
    Generative AI: GPT-3.5.
    Prompt used: I have this error "IndexError: index 1001 is out of the bounds for axis 1 with size 1001" this is the code [.....].
    Usage Explanation: fixing the errors that I have encountered.
    Justification: I would like to understand more about the errors that occurred and how they could be handled.
"""

# Zoom_image function 
# Adapted from: "Implementing Bilinear Interpolation for Image Resizing" by Meghal Darji
# Link: https://meghal-darji.medium.com/implementing-bilinear-interpolation-for-image-resizing-357cbb2c2722 

def zoom_image(image, zoom_factor):
    """
    Applies a zoom effect to the original image based on the provided zoom factor using bilinear interpolation.
    Arguments:
        image (numpy.ndarray): The 2D grayscale input image.
        zoom_factor (float): it determines the degree of zoom applied to the image. If it is greater than 1 will 
        enlarge the image, while it is less than 1 will shrink the image.
    Returns:
        new_array (numpy.ndarray): The 2D grayscale image that has been zoomed.
    Exceptions:
        None
    """
    # get the size of the original image.
    rows, cols = image.shape
    # create the new array with new dimensions.
    new_rows = int(rows * zoom_factor)
    new_cols = int(cols * zoom_factor)
    new_array = np.zeros((new_rows, new_cols))
    # map output image coordinates (x, y) to corresponding input image coordinates (x', y').
    for i in range(new_rows):
        for j in range(new_cols):
            original_row = i / zoom_factor
            original_col = j / zoom_factor
            new_array[i, j] = __bilinear_interpolation(image, original_row, original_col)
    # return the zoomed image.
    return new_array

# Bilinear_interpolation function 
# Adapted from: "Implementing Bilinear Interpolation for Image Resizing" by Meghal Darji
# Link: https://meghal-darji.medium.com/implementing-bilinear-interpolation-for-image-resizing-357cbb2c2722 

def __bilinear_interpolation(image, x, y):
    """
    Applies bilinear interpolation to the original image to estimate unknown values (pixels) based on known ones.
    Arguments:
        image (numpy.ndarray): the 2D grayscale input image.
        x (float): the intended point for interpolation, specified the x-coordinate.
        y (float): the intended point for interpolation, specified the  y-coordinate.
    Returns:
        pixel_value (float): the estimated pixel value using bilinear interpolation at the given coordinate.
    Exceptions:
        None
    """
    # get the size of the original image.
    rows, cols = image.shape
    # calculate the positions of the 4 nearest pixels for (x,y) within the image boundaries. 
    x_floor = int(np.floor(x))
    x_ceil = min(x_floor + 1, rows - 1)
    y_floor = int(np.floor(y))
    y_ceil = min(y_floor + 1, cols - 1)
    # get the pixels values from the original image surrounding pixel at (x,y).
    q11 = image[x_floor, y_floor]
    q12 = image[x_floor, y_ceil]
    q21 = image[x_ceil, y_floor]
    q22 = image[x_ceil, y_ceil]
    # calculate the differences between x and x_floor, and y and y_floor to get the fraction,
    # these fractions indicate the relative position of the input coordinates within the pixel grid.
    x_diff = x - x_floor
    y_diff = y - y_floor
    # estimate the pixel value using the bilinear interpolation equation that depends on the pixel values of the neighbors.
    pixel_value = (q11 * (1 - x_diff) * (1 - y_diff) 
         + q12 * (1 - x_diff) * y_diff 
         + q21 * x_diff * (1 - y_diff)
         + q22 * x_diff * y_diff)
    # return the estimated pixel value at the given coordinate.
    return pixel_value

# Rotate_image function 
# Adapted from: "Rotating Image By Any Angle(Shear Transformation) Using Only NumPy" by Gautam Agrawal
# Link: https://gautamnagrawal.medium.com/rotating-image-by-any-angle-shear-transformation-using-only-numpy-d28d16eb5076 

def rotate_image(image, angle):
    """
    Applies a rotating effect to the original image based on the provided rotation angle (in degrees) using bilinear interpolation.
    Arguments:
        image (numpy.ndarray): the 2D grayscale input image.
        angle (float): the angle of rotation in degrees.
    Returns:
        new_array (numpy.ndarray): The 2D grayscale image that has been rotated.
    Exceptions:
        None
    """
    # convert angle from degrees to radians.
    angle_radians = math.radians(angle)
    # get the size of the original image.
    height, width = image.shape
    # calculate the dimensions of the new image
    cosine = math.cos(angle_radians)
    sine = math.sin(angle_radians)
    new_height = round(height * abs(cosine) + width * abs(sine))
    new_width = round(width * abs(cosine) + height * abs(sine))
    # create a new image
    output = np.zeros((new_height, new_width), dtype=np.uint8)
    # calculate the centers of the original and new images
    original_center = np.array([(width - 1) / 2, (height - 1) / 2])
    new_center = np.array([(new_width - 1) / 2, (new_height - 1) / 2])
    # apply rotation transformation to each pixel
    for y in range(new_height):
        for x in range(new_width):
            # calculate the coordinates relative to the new center
            x_to_center = x - new_center[0]
            y_to_center = y - new_center[1]
            # apply inverse rotation transformation
            rotated_coords = np.array([x_to_center, y_to_center])
            original_coords = np.dot(np.array([[cosine, -sine], [sine, cosine]]), rotated_coords)
            # calculate the coordinates relative to the original center
            original_coords_with_center = original_center + original_coords
            # check if the original coordinates are within the image bounds
            if 0 <= original_coords_with_center[1] < height - 1 and 0 <= original_coords_with_center[0] < width - 1:
                output[y, x] = __bilinear_interpolation(image, original_coords_with_center[1] ,original_coords_with_center[0])
    return output
