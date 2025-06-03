import cv2

# Görüntüyü oku
img = cv2.imread("C:/Users/MUSA/Desktop/OpenCV/GoruntuEsikleme/indir (2).jpeg")

# Görüntünün başarıyla okunup okunmadığını kontrol et
if img is None:
    print("Hata: Görüntü okunamadi! Dosya yolunu kontrol et.")
    exit()

   
# Gri tonlamaya çevir
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Basit eşikleme
_, thresh_img = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)

"""
Eşikleme (Thresholding), piksellerin belirli bir değere göre siyah veya beyaz olarak değiştirilmesini sağlar.
cv2.threshold() fonksiyonu kullanilir
Parametreler:
img: Gri tonlamali giriş görüntüsü.
60: Eşik değeri → 60’tan küçük pikseller siyah (0), büyük olanlar beyaz (255) yapilir.
255: Maksimum parlaklik değeri (beyaz).
cv2.THRESH_BINARY: İkili eşikleme (binary thresholding) uygular.
Dönen Değerler:
_: Kullanilmayan eşik değeri (genellikle gereksiz).
thresh_img: Eşiklenmiş görüntü.
"""

# Adaptif eşikleme
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

"""
Basit eşikleme sabit bir eşik değeri (örn. 60) kullanirken, adaptif eşikleme görüntünün farkli bölgelerindeki aydinlatma değişimlerine daha iyi uyum sağlar.
Parametreler:
img: Gri tonlamali giriş görüntüsü.
255: Maksimum parlaklik değeri.
cv2.ADAPTIVE_THRESH_MEAN_C: Her piksel için eşik değeri, çevresindeki piksellerin ortalamasi alinarak hesaplanir.
cv2.THRESH_BINARY: İkili eşikleme uygulanir.
11: Çevresel pencere boyutu (blok büyüklüğü) → Her piksel için eşik değeri hesaplanirken 11x11’lik bir bölge kullanilir.
8: Ortalama değerden çikarilacak sabit bir değer (C).
"""

# Her görüntüyü farklı pencerelerde aç
cv2.imshow("Gri Tonlamali Görüntü", img)
cv2.imshow("Basit Eşikleme", thresh_img)
cv2.imshow("Adaptif Eşikleme", thresh_img2)

# Pencerelerin konumunu ayarla (görünmeme sorununu çözer)
cv2.moveWindow("Gri Tonlamali Görüntü", 100, 100)
cv2.moveWindow("Basit Eşikleme", 400, 100)
cv2.moveWindow("Adaptif Eşikleme", 700, 100)

"""
OpenCV, pencereleri rastgele yerleştirebilir.
cv2.moveWindow(pencere_adi, x, y) fonksiyonu ile pencerelerin ekrandaki konumlari belirlenir.
"Gri Tonlamali Görüntü" (100,100) koordinatinda, "Basit Eşikleme" (400,100) ve "Adaptif Eşikleme" (700,100) konumuna taşinir.
"""

# Pencerelerin açık kalmasını sağla
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
🔹 KODUN GENEL İŞLEYİŞİ
1️⃣ Görüntü dosyasi okunur ve gri tonlamaya çevrilir.
2️⃣ Basit eşikleme (sabit eşik değeri ile) uygulanir.
3️⃣ Adaptif eşikleme (piksellere göre değişen eşik değeri) uygulanir.
4️⃣ Üç ayri pencere açilir:

Gri tonlamali görüntü
Basit eşiklenmiş görüntü
Adaptif eşiklenmiş görüntü
5️⃣ Pencereler farkli konumlara taşinir.
6️⃣ Kullanici bir tuşa basana kadar pencereler açik kalir.
🚀 ÇIKTI
Bu kodu çaliştirdiğinda ekranda üç ayri pencere açilacaktir:
✅ Gri Tonlamali Görüntü
✅ Basit Eşikleme (Sabit değerle siyah-beyaz ayrimi)
✅ Adaptif Eşikleme (Yerel parlakliğa göre eşikleme)

📌 Bir tuşa bastiğinda pencereler kapanacaktir.
"""
