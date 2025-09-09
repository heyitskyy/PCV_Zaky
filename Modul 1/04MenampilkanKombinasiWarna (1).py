import cv2
import copy 

# Membaca File Citra
imageBGR = cv2.imread("itsSurabaya2.jpg")
#Menampilkan Warna Merah 
image = copy.deepcopy(imageBGR)
image[:,:,0]=0 
image[:,:,1]=0
cv2.imshow("Image Merah", image) 
#Menampilkan Warna Hijau 
image = copy.deepcopy(imageBGR)
image[:,:,0]=0 
image[:,:,2]=0
cv2.imshow("Image Hijau", image) 
#Menampilkan Warna Biru 
image = copy.deepcopy(imageBGR)
image[:,:,1]=0 
image[:,:,2]=0
# Menampilkan Citra
cv2.imshow("Image Biru", image) 

#Menampilkan Kombinasi Merah Hijau
image = copy.deepcopy(imageBGR)
image[:,:,2]=0 
cv2.imshow("Image Kombinasi Merah Hijau", image) 
#Menampilkan Kombinasi Merah Biru
image = copy.deepcopy(imageBGR)
image[:,:,1]=0 
cv2.imshow("Image Kombinasi Merah Biru", image) 
#Menampilkan Kombinasi Hijau Biru
image = copy.deepcopy(imageBGR)
image[:,:,0]=0 
cv2.imshow("Image Kombinasi Hijau  Biru", image) 
#Menampilkan Kombinasi Merah Hijau Biru
image = copy.deepcopy(imageBGR)
cv2.imshow("Image Kombinasi Merah Hijau  Biru", image) 

# Menunggu sampai tombol di tekan
cv2.waitKey(0)
 
# Menutup semua window
cv2.destroyAllWindows()