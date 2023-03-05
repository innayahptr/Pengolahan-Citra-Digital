# import module
from PIL import Image, ImageChops

#Membaca gambar yang akan di proses
img1 = Image.open("imgd1.jpg")
img2 = Image.open("imgd2.jpg")

#Mencari perbedaan
diff = ImageChops.difference(img1, img2)

#Menampilkan perbedaan
diff.show()
