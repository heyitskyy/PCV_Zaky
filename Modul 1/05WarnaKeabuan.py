import cv2
import copy 
import numpy as np 
# Membaca File Citra
imageBGR = cv2.imread("Kyy2.jpg")

print("Tipe Data :", imageBGR.dtype)
print("Konversi dari tipe data uint8 ke tipe data float64")
(r,c,d)=imageBGR.shape 
imageBGRf64 = imageBGR.astype(np.float64)
#Menyimpan layer warna ke masing-masing variabel  
ImageR = imageBGRf64[:,:,2]
ImageG = imageBGRf64[:,:,1]
ImageB = imageBGRf64[:,:,0]

Image=np.floor((ImageR+ImageG+ImageB)/3)
#Menyiapkan Penampung dengan dimensi yang sama dengan imageBGR untuk citra keabuan
ImageGray =np.zeros((r,c,d))
#Meletakan Image ke masing-masing layer warna BGR p
ImageGray[:,:,0]=Image[:,:]
ImageGray[:,:,1]=Image[:,:]
ImageGray[:,:,2]=Image[:,:]

#Mengkonversi citra bertipe data float64 ke uint8
ImageGray = ImageGray.astype(np.uint8) 
cv2.imshow("Citra Keabuan", ImageGray)

# Menunggu sampai tombol di tekan
cv2.waitKey(0)
# Menutup semua window
cv2.destroyAllWindows()