##################################################
#nama file program :MembacaFileDanMenampilkan.py
#Program Untuk Membaca dan menampilkan file CITRA
#################################################

#Import library opencv
import cv2
import copy

# Membaca File Citra
imageBGR = cv2.imread("Kyy2.jpg")

image = copy.deepcopy(imageBGR)
cv2.imshow("Asli", image)

image = copy.deepcopy(imageBGR)
image[:,:,0]=0 
image[:,:,1]=0
cv2.imshow("Merah", image) 

image = copy.deepcopy(imageBGR)
image[:,:,1]=0
image[:,:,2]=0
cv2.imshow("Biru", image) 

image = copy.deepcopy(imageBGR)
image[:,:,0]=0
image[:,:,2]=0
cv2.imshow("Hijau", image) 

image = copy.deepcopy(imageBGR)
image[:,:,0]=0
cv2.imshow("Mix 1", image) 

image = copy.deepcopy(imageBGR)
image[:,:,1]=0
cv2.imshow("Mix 2", image) 

image = copy.deepcopy(imageBGR)
image[:,:,2]=0
cv2.imshow("Mix 3", image) 

neg = 255 - imageBGR
cv2.imshow("Negative", neg)

# Menunggu sampai tombol di tekan
cv2.waitKey(0)
 
# Menutup semua window
cv2.destroyAllWindows()