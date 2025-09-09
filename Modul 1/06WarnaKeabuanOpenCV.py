import cv2

# Membaca File Citra
ImageBGR = cv2.imread("Kyy2.jpg")
#Mengkonversi Dari BGR ke Gray   
ImageGray = cv2.cvtColor(ImageBGR, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Image BGR',ImageBGR)
cv2.imshow('Gray image', ImageGray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
