import cv2

#Membaca gambar yang akan di proses
gambar =cv2.imread("imgmawar.jpg")

#Taking Kernel size as 5x5
gaussian_blur = cv2.GaussianBlur(gambar,(5,5),sigmaX=0)

#Menampilkan hasil proses dengan metode gaussian blur
window_name='image averaging'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow ('original image', gambar)
cv2.imshow(window_name,gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
