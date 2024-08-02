# Bilinear-Interpolation-Zoom-Rotate 🔍🔄

## Overview 🌐

**Bilinear Interpolation** is a technique used in image processing for the purpose of image scaling and rotation. When an image is scaled up or down (zoomed in or out), the pixels in the original image need to be resized to fit the new dimensions. Bilinear Interpolation is a method for determining the new pixel values during this scaling process.

The basic idea behind **Bilinear Interpolation** is to take the four closest known pixel values around the desired new pixel location, and then calculate the new pixel value based on a weighted average of those four values. This results in a smoother, more natural-looking scaled image compared to simpler interpolation methods like Nearest Neighbor.

## Screenshots 📷
1. Original 

![test](https://github.com/user-attachments/assets/cfb6ca51-d9b3-4e3a-9ef5-bc82943629e2)

2. Zoom in

![output_image(1)](https://github.com/user-attachments/assets/2a5e69b5-b029-49bd-904d-92c0d9e70e7e)

3. Zoom out

![output_image(2)](https://github.com/user-attachments/assets/aa0e9f9c-11de-4521-aa8c-42bb86e1a42d)

4. Rotation

![output_image(3)](https://github.com/user-attachments/assets/f4e367c1-0535-4eb5-8fed-13f9fb233da5)


## How to Run ⚙️
1. Clone the repository.
```
git clone 
```
2. run main.py file
```
python main.py
```
*Note*: This small application works only with grayscale images with one dimension.

## Contributor ✍️
- Salwa Shamma
