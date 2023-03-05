import cv2
import numpy as np
import matplotlib.pyplot as plt

#Membaca gambar yang akan di proses
gambar = cv2.imread('imgmawar.jpg', 0)

#Deklarasi histogram equalisation
equ = cv2.equalizeHist(gambar)

#Menampilkan hasil
plt.subplot(121), plt.imshow(gambar, cmap='gray')
plt.title('Original Image')
plt.subplot(122), plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')
plt.show()
