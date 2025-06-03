import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
cv2 (OpenCV) → Görüntü işleme için kullaniliyor.
matplotlib.pyplot → Görüntüleri göstermek için kullaniliyor.
numpy → Matris işlemleri ve kernel oluşturma gibi işlemler için kullaniliyor.
"""

# Görüntüyü oku (Grayscale)
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\MorfolojikOperasyonlar\data.png", 0)

"""
cv2.imread(path, 0) → Görüntüyü gri tonlamali (grayscale) olarak okur.
Eğer 0 yerine 1 kullanilsaydi, görüntü renkli olarak okunurdu.
"""

# Eğer görüntü okunamazsa hata mesajı ver
if img is None:
    print("Görüntü dosyasi bulunamadi, dosya yolunu kontrol edin!")

    """
    Eğer görüntü yüklenemezse (yanliş dosya yolu veya eksik dosya), hata mesaji verilir.

    """
else:
    plt.figure()
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.title("Orijinal Img")

    """
    plt.figure() → Yeni bir çizim oluşturur.
    plt.imshow(img, cmap="gray") → Görüntüyü gri tonlamali olarak gösterir.
    plt.axis("off") → X ve Y eksenlerini gizler.
    plt.title("Orijinal Img") → Başlik ekler.
    """

    # Erozyon işlemi
    kernel = np.ones((5, 5), dtype=np.uint8)
    result = cv2.erode(img, kernel, iterations=1)
    plt.figure()
    plt.imshow(result, cmap="gray")
    plt.axis("off")
    plt.title("Erozyon")

    """
    Erozyon, görüntüdeki beyaz alanlari küçültür (gürültüyü azaltmak veya ince detaylari kaldirmak için kullanilir).
    kernel = np.ones((5,5), dtype=np.uint8) → 5x5 boyutunda bir beyaz (1) kare matrisi oluşturur.
    cv2.erode(img, kernel, iterations=1) → Kernel, görüntü üzerinde dolaşarak beyaz pikselleri küçültür.
    """

    # Genişletme işlemi (Dilation)
    result2 = cv2.dilate(img, kernel, iterations=1)
    plt.figure()
    plt.imshow(result2, cmap="gray")
    plt.axis("off")
    plt.title("Genişletme")

    """
    Genişletme (Dilation), görüntüdeki beyaz alanlari genişletir (boşluklari doldurmak için kullanilir).
    cv2.dilate(img, kernel, iterations=1) → Kernel, görüntü üzerinde dolaşarak beyaz pikselleri büyütür.
    """

    # Beyaz gürültü (White Noise)
    whiteNoise = (np.random.randint(0, 2, size=img.shape[:2], dtype=np.uint8) * 255)
    plt.figure()
    plt.imshow(whiteNoise, cmap="gray")
    plt.axis("off")
    plt.title("White Noise")

    """
    Beyaz gürültü, rastgele 0 ve 255 değerlerinden oluşan bir matristir.
    np.random.randint(0, 2, size=img.shape[:2], dtype=np.uint8) → 0 veya 1 içeren bir matris oluşturur.
    * 255 → 1'leri 255 (beyaz) yapar, 0'lari siyah olarak birakir.
    """

    # Beyaz gürültü eklenmiş görüntü
    noise_img = cv2.add(img, whiteNoise)  # Doğrudan OpenCV ekleme fonksiyonu kullan
    plt.figure()
    plt.imshow(noise_img, cmap="gray")
    plt.axis("off")
    plt.title("Img With White Noise")

    """
    cv2.add() → OpenCV'nin güvenli toplama fonksiyonudur.
    Gürültü + Orijinal Görüntü = Gürültülü Görüntü
    """

    # Açma (Opening)
    opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
    plt.figure()
    plt.imshow(opening, cmap="gray")
    plt.axis("off")
    plt.title("Açma")

    """
    Açma (Opening) işlemi, erozyon + genişletme işlemlerini sirasiyla uygular.
    Beyaz gürültüyü (white noise) temizlemek için kullanilir.
    """

    # Siyah gürültü (Black Noise)
    blackNoise = (np.random.randint(0, 2, size=img.shape[:2], dtype=np.uint8) * 255)
    blackNoise = blackNoise.astype(np.int16)  # Negatif değerler için
    black_noise_img = img.astype(np.int16) - blackNoise
    black_noise_img[black_noise_img < 0] = 0  # Negatif değerleri sıfıra ayarla
    black_noise_img = black_noise_img.astype(np.uint8)  # Geri çevir

    """
    Siyah gürültü, rastgele 0 ve -255 değerlerinden oluşur.
    astype(np.int16) → Negatif değerler oluşturmak için veri tipi değiştirilir.
    Orijinal görüntü - Siyah gürültü → Siyah noktalar eklenmiş görüntü.
    Negatif değerler sifira ayarlanir (çünkü uint8 veri tipi negatif desteklemez).
    """

    plt.figure()
    plt.imshow(blackNoise, cmap="gray")
    plt.axis("off")
    plt.title("Black Noise")

    plt.figure()
    plt.imshow(black_noise_img, cmap="gray")
    plt.axis("off")
    plt.title("Black Noise Img")

    # Kapatma (Closing)
    closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
    """
    Kapatma (Closing) işlemi, genişletme + erozyon işlemlerini sirasiyla uygular.
    Siyah gürültüyü (black noise) temizlemek için kullanilir.
    """
    plt.figure()
    plt.imshow(closing, cmap="gray")
    plt.axis("off")
    plt.title("Kapama")

    # Morfolojik Gradyan
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    """
    Gradyan, genişletme ve erozyon arasindaki farki hesaplar.
    Kenar belirleme işlemlerinde kullanilir.
    """
    plt.figure()
    plt.imshow(gradient, cmap="gray")
    plt.axis("off")
    plt.title("Gradyan")

    plt.show()
    """
    Bütün çizimleri ekrana getirir.
    """


    """
    📌 Bu kod OpenCV ile temel morfolojik işlemleri uygular:
    ✅ Erozyon → Beyaz pikselleri küçültür.
    ✅ Genişletme → Beyaz pikselleri büyütür.
    ✅ Beyaz Gürültü → Rastgele beyaz noktalar ekler.
    ✅ Açma (Opening) → Beyaz gürültüyü temizler.
    ✅ Siyah Gürültü → Rastgele siyah noktalar ekler.
    ✅ Kapatma (Closing) → Siyah gürültüyü temizler.
    ✅ Gradyan → Görüntünün kenarlarini belirler.

    🚀 Bu işlemler, görüntü işlemede gürültü temizleme ve kenar belirleme gibi önemli adimlardir.
    """
