import cv2
import numpy as np

# Load the image
img = cv2.imread('noise.jpg')

# Define kernel for min filter
kernel = np.ones((3, 3), np.uint8)

# Apply min filter
min_filtered = cv2.erode(img, kernel, iterations=1)

# Display the original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Min Filtered Image', min_filtered)

# Wait for key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
