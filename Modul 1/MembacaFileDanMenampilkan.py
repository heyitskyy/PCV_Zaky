##################################################
#nama file program :MembacaFileDanMenampilkan.py
#Program Untuk Membaca dan menampilkan file CITRA
#################################################

#Import library opencv
import cv2

# Membaca File Citra
image = cv2.imread("itsSurabaya2.jpg")
# Menampilkan Citra
cv2.imshow("Image", image)

#Menampilkan dimensi citra

#r = tinggi citra 
r = image.shape[0]
#c = Lebar citra 
c = image.shape[1]
#d = Kedalaman Citra
d = image.shape[2]
print("Dimensi Citra :", r,c,d)

# Menunggu sampai tombol di tekan
cv2.waitKey(0)
 
# Menutup semua window
cv2.destroyAllWindows()