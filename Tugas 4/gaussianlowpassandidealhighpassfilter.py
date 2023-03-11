import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('mawar.png', 0)

# Compute the DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create the Gaussian lowpass filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
sigma = 30  # Standard deviation of the filter
gaussian_mask = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        gaussian_mask[i, j, 0] = np.exp(-dist**2 / (2*sigma**2))
        gaussian_mask[i, j, 1] = np.exp(-dist**2 / (2*sigma**2))

# Apply the Gaussian lowpass filter
dft_filtered = dft_shift * gaussian_mask

# Compute the inverse DFT
img_filtered = cv2.idft(np.fft.ifftshift(dft_filtered))
img_filtered = cv2.magnitude(img_filtered[:, :, 0], img_filtered[:, :, 1])

# Display the filtered image
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_filtered, cmap='gray')
plt.title('Gaussian Lowpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()

# Create the ideal highpass filter
r = 30  # Radius of the filter
mask = np.ones((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        if dist <= r:
            mask[i, j, 0] = 0
            mask[i, j, 1] = 0

# Apply the ideal highpass filter
dft_filtered = dft_shift * mask

# Compute the inverse DFT
img_filtered = cv2.idft(np.fft.ifftshift(dft_filtered))
img_filtered = cv2.magnitude(img_filtered[:, :, 0], img_filtered[:, :, 1])

# Display the filtered image
plt.imshow(img_filtered, cmap='gray')
plt.title('Ideal Highpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
