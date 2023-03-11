import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('greynoise.jpg', 0)

# Compute the FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Compute the magnitude spectrum
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Display the original and magnitude spectrum
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
