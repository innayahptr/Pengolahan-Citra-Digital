import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('mawar.png', 0)

# Compute the DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create a mask for the highpass filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
r = 50  # Radius of the filter
bhpf = np.zeros((rows, cols, 2), np.float32)
ghpf = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        dist = np.sqrt((i-crow)**2 + (j-ccol)**2)
        bhpf[i, j, 0] = 1 / (1 + (r/dist)**(2*4))  # 4th order Butterworth highpass filter
        ghpf[i, j, 0] = 1 - np.exp(-((dist**2)/(2*(r**2))))  # Gaussian highpass filter
        bhpf[i, j, 1] = bhpf[i, j, 0]
        ghpf[i, j, 1] = ghpf[i, j, 0]

# Apply the Butterworth Highpass Filter
dft_shift_bhpf = dft_shift * bhpf
bhpf = np.fft.ifftshift(dft_shift_bhpf)
bhpf = cv2.idft(bhpf)
bhpf = cv2.magnitude(bhpf[:, :, 0], bhpf[:, :, 1])

# Apply the Gaussian Highpass Filter
dft_shift_ghpf = dft_shift * ghpf
ghpf = np.fft.ifftshift(dft_shift_ghpf)
ghpf = cv2.idft(ghpf)
ghpf = cv2.magnitude(ghpf[:, :, 0], ghpf[:, :, 1])

# Display the original, Butterworth Highpass Filter, and Gaussian Highpass Filter
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(bhpf, cmap='gray')
plt.title('Butterworth Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(ghpf, cmap='gray')
plt.title('Gaussian Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()
