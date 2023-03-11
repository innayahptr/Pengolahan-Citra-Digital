import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('mawar.png', 0)

# Compute the DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create the ideal lowpass filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
r = 30  # Radius of the filter
mask = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        if dist <= r:
            mask[i, j, 0] = 1
            mask[i, j, 1] = 1

# Apply the ideal lowpass filter
dft_filtered = dft_shift * mask

# Compute the inverse DFT
img_filtered = cv2.idft(np.fft.ifftshift(dft_filtered))
img_filtered = cv2.magnitude(img_filtered[:, :, 0], img_filtered[:, :, 1])

# Display the original and filtered image
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_filtered, cmap='gray')
plt.title('Ideal Lowpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()

# Create the Butterworth lowpass filter
n = 2  # Order of the filter
d0 = 30  # Cutoff frequency
butterworth_mask = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        butterworth_mask[i, j, 0] = 1 / (1 + (dist/d0)**(2*n))
        butterworth_mask[i, j, 1] = 1 / (1 + (dist/d0)**(2*n))

# Apply the Butterworth lowpass filter
dft_filtered = dft_shift * butterworth_mask

# Compute the inverse DFT
img_filtered = cv2.idft(np.fft.ifftshift(dft_filtered))
img_filtered = cv2.magnitude(img_filtered[:, :, 0], img_filtered[:, :, 1])

# Display the filtered image
plt.imshow(img_filtered, cmap='gray')
plt.title('Butterworth Lowpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
