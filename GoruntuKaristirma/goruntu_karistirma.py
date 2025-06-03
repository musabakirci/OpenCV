import cv2
import matplotlib.pyplot as plt

"""
cv2 (OpenCV): Görüntü işleme işlemlerini yapmak için kullaniliyor.
matplotlib.pyplot: Görüntüleri grafik olarak göstermek için kullaniliyor.

"""

# Görüntüleri oku
img1 = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\GoruntuKaristirma\indir.jpeg")
img2 = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\GoruntuKaristirma\indir (1).jpeg")

# Görüntüleri RGB formatına çevir
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

"""
OpenCV, görüntüleri BGR (Blue-Green-Red) formatinda okur.
cv2.cvtColor(img, cv2.COLOR_BGR2RGB) ile görüntüler RGB formatina çevrilerek
matplotlib ile doğru renkte gösterilmesi sağlaniyor.
"""

# Görüntü boyutlarını eşitle (eğer farklı boyutlardaysa)
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

"""
Görüntülerin boyutlari farkli olabilir.
cv2.resize() fonksiyonu ile her iki görüntü de (500, 500) piksel boyutuna getirilerek kariştirma işlemi için uyumlu hale getiriliyor.

"""

# Görüntüleri karıştır (alpha: 0.5, beta: 0.5)
blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

"""
cv2.addWeighted(src1, alpha, src2, beta, gamma) fonksiyonu ile görüntüler belirli oranlarda birleştiriliyor.
Parametreler:
img1: İlk görüntü
0.5: İlk görüntünün ağirliği (alpha)
img2: İkinci görüntü
0.5: İkinci görüntünün ağirliği (beta)
0: Parlaklik ayari (gamma) – burada kullanilmiyor.
Bu işlem, iki görüntüyü %50 - %50 oraninda harmanlayarak yeni bir görüntü oluşturuyor.
"""

# Görüntüleri göster
plt.figure(figsize=(10, 5))

"""
plt.figure(figsize=(10, 5)): Grafik penceresinin boyutunu ayarlar (10x5 inç).
"""

plt.subplot(1, 3, 1)
plt.imshow(img1)
plt.title("Görüntü 1")
plt.axis("off")

"""
plt.subplot(1, 3, 1): 1 satir, 3 sütundan oluşan bir grafik alani oluşturur ve ilk konumu seçer.
plt.imshow(img1): İlk görüntüyü gösterir.
plt.title("Görüntü 1"): Başlik ekler.
plt.axis("off"): Eksen çizgilerini kaldirir.
"""

plt.subplot(1, 3, 2)
plt.imshow(img2)
plt.title("Görüntü 2")
plt.axis("off")

"""
Ayni işlemler ikinci görüntü için de yapiliyor:
"""

plt.subplot(1, 3, 3)
plt.imshow(blended)
plt.title("Kariştirilmiş Görüntü")
plt.axis("off")

plt.show()


"""
Özet
Bu kod:
✅ OpenCV ile iki görüntüyü okur.
✅ Görüntüleri RGB formatina çevirir.
✅ Boyutlarini 500x500 piksele ayarlar.
✅ cv2.addWeighted() fonksiyonu ile iki görüntüyü %50-%50 oraninda birleştirir.
✅ Matplotlib ile üç görüntüyü (orijinal iki görüntü + kariştirilmi ş görüntü) ekranda gösterir.

Kodun çiktisi, üç yan yana görüntü olacak şekilde:
1️⃣ İlk görüntü
2️⃣ İkinci görüntü
3️⃣ Kariştirilmiş görüntü
"""