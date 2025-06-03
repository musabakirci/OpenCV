import cv2
import numpy as np

# Resim oluştur
img = np.zeros((512,512,3), np.uint8) # siyah bir resim
print(img.shape)

cv2.imshow("Siyah", img)

# Çizgi
#(resim, başlangıç noktası, bitiş noktası,renk, kalinlik)
cv2.line(img, (100,100), (100,300), (0,255,0), 3) 
cv2.imshow("Cizgi", img)

# Dikdörtgen
# (resim, başlangiç, bitiş, renk )
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)

# çember
# (resim, merkez, yariçap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)

# Metin
# (resim, başlangıç noktası, font, kalinliği, renk)
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)

# Pencerelerin açık kalmasını sağla
cv2.waitKey(0)  
cv2.destroyAllWindows()

"""
    cv2.waitKey(0): Bir tuşa basilana kadar bekler. Bu, görüntü penceresinin açik kalmasini sağlar.
    cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatir. Bir tuşa basildiğinda tüm pencereler kapanir.
"""
