import cv2

# Load the image
img = cv2.imread('noise.jpg')

# Apply median filter with kernel size 3
median = cv2.medianBlur(img, 3)

# Display the original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', median)

# Wait for key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
