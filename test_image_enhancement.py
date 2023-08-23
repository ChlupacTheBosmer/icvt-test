
import cv2
from cv2 import dnn_superres


def esrgan(input_frame):
    # Load the pre-trained ESRGAN model
    esrgan = dnn_superres.DnnSuperResImpl_create()
    esrgan.readModel('FSRCNN_x2.pb')
    esrgan.setModel('fsrcnn', 2)

    # Perform super-resolution
    output_frame = esrgan.upsample(input_frame)

    # Save the super-resolved image
    cv2.imwrite('output_frame.jpg', output_frame)

    return output_frame

def is_blurred(image, threshold=100):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian gradient magnitude
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    gradient_magnitude = cv2.convertScaleAbs(laplacian)

    # Calculate the mean gradient magnitude
    mean_gradient = cv2.mean(gradient_magnitude)[0]

    # Compare the mean gradient magnitude with the threshold
    if mean_gradient < threshold:
        return True  # Image is blurred
    else:
        return False  # Image is sharp

def enhance_focus(image):
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(image, (0, 0), 3)

    # Subtract the blurred image from the original image to get edges
    edges = cv2.subtract(image, blurred)

    # Scale the edges to enhance contrast
    enhanced = cv2.addWeighted(image, 1.5, edges, -0.5, 0)

    return enhanced


def shrapen(image):
    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Save the image
    cv2.imwrite('sharpened_image.jpg', sharpened_image)

    return sharpened_image

def unsharp_mask(image, amount=1.0, radius=1.0):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred = cv2.GaussianBlur(gray, (0, 0), radius)

    # Calculate the sharpened image by subtracting the blurred image from the original
    sharpened = cv2.addWeighted(gray, 1 + amount, blurred, -amount, 0)

    return sharpened

# Load your image
input_image = cv2.imread(r"CZ2_M2_ErySpp03_20210616_16_12_1_1960_0_340,37_980,677.jpg")

# Set a threshold for blur detection
blur_threshold = 50

# Check if the image is blurred
if is_blurred(input_image, blur_threshold):
    print("Image is blurred or not focused enough.")
    try:
        input_image = esrgan(input_image)
    except:
        raise
    input_image = shrapen(input_image)
else:
    print("Image is sharp.")

# Enhance the focus of the image
enhanced_image = enhance_focus(input_image)

# Save the enhanced image
cv2.imwrite('enhanced_image.jpg', enhanced_image)

# Define the target size (640x640)
target_size = (640, 640)

# Resize the image
resized_image = cv2.resize(input_image, target_size)

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)


# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# # Load the image
# image = cv2.imread(r"CZ2_M2_ErySpp03_20210616_16_12_1_1960_0_340,37_980,677.jpg")
#
# # Plot the original image
# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(image)


# # Plot the sharpened image
# plt.subplot(1, 2, 2)
# plt.title("Sharpening")
# plt.imshow(sharpened_image)
# plt.show()