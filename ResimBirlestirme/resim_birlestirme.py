import cv2
import numpy as np

# resmi ice aktar
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\ResimBirlestirme\Ataturk.jpg")
cv2.imshow("Orijinal", img)

# yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal(Yan yana)", hor)

# dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical(dikey)",ver)



# Pencerelerin açık kalmasını sağla
cv2.waitKey(0)  
cv2.destroyAllWindows()

