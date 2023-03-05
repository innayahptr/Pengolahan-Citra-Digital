import cv2
import numpy as np
import matplotlib.pyplot as plt

#Membaca gambar yang akan di proses
gambar = cv2.imread('histoimg.jpg', 0)

#Hitung histogram
hist, bins = np.histogram(gambar.flatten(), 256, [0,256])

#Plot histogram
plt.hist(gambar.flatten(), 256, [0,256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
cv2.imshow('Image', gambar)
plt.show()
