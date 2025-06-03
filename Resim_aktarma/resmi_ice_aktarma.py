import cv2

# Resmi içe aktar
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\indir.jpeg", 0)

# Görselleştirme
cv2.imshow("I lk Resim", img)

# Bir tuşa basılmasını bekleyin
k = cv2.waitKey(0) & 0xFF
"""
cv2.waitKey(0) & 0xFF Kullanimi
Verdiğiniz kodda: cv2.waitKey(0) & 0xFF ifadesi, tuşa basildiğinda bu tuşun 
ASCII değerini almak için kullanilir. Bu, daha geniş platform uyumluluğu sağlamak 
amaciyla kullanilir (bazi platformlarda 32-bit veri dönebilir, bu nedenle & 0xFF 
ile sadece 8-bit değer alinir)."""

# Tüm pencereleri kapatın
if k == 27: # 
    # 27 esc tuşunun ASKII değeri. esc ye basınca görüntü kapanacak
    cv2.destroyAllWindows()

elif k == ord("s"):
    #ord("s"), "s" tuşunun ASCII değerini alır. s tuşuna basarsa resmi kaydeder.
    cv2.imwrite("messi_gray.png", img)   
    cv2.destroyAllWindows()