import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('mawar.png', 0)

# Apply Unsharp Masking filter
blur = cv2.GaussianBlur(img, (5, 5), 0)
unsharp_img = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

# Compute the Laplacian of the image in frequency domain
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
dft_laplacian = cv2.filter2D(dft_shift, -1, laplacian_kernel)

# Apply Selective Filtering
rows, cols = img.shape
crow, ccol = rows//2, cols//2
r = 30  # Radius of the filter
mask = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        if dist > r:
            mask[i, j, 0] = 1
            mask[i, j, 1] = 1
dft_selective = dft_shift * mask

# Compute the inverse DFT
img_unsharp = cv2.idft(np.fft.ifftshift(dft_laplacian))
img_selective = cv2.idft(np.fft.ifftshift(dft_selective))

# Display the original, Unsharp Masking, Laplacian Filter, and Selective Filtering
plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(unsharp_img, cmap='gray')
plt.title('Unsharp Masking'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img_unsharp[:, :, 0], cmap='gray')
plt.title('Laplacian Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_selective[:, :, 0], cmap='gray')
plt.title('Selective Filtering'), plt.xticks([]), plt.yticks([])
plt.show()
