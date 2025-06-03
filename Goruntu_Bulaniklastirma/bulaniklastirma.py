import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

"""
cv2: OpenCV kütüphanesi, görüntü işleme ve bilgisayarla görme (computer vision) için kullanilir.
matplotlib.pyplot: Görüntülerin görselleştirilmesi için kullanilir. imshow fonksiyonu ile görüntüleri gösterir.
numpy: Sayisal hesaplamalar yapmak ve veri yapilari oluşturmak için kullanilir.
warnings: Uyarilari gizler, bu sayede bazi işlemler sirasinda kullaniciya gösterilen uyarilari engeller.
"""

# Uyarıları gizle
warnings.filterwarnings("ignore")

# Resmi oku
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Goruntu_Bulaniklastirma\gorseller-6-m.jpg")

# Eğer resim okunamazsa hata mesajı yazdır
if img is None:
    print("Resim okunamadi, dosya yolunu kontrol edin!")
else:
    # BGR'yi RGB'ye çevir
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    """
    OpenCV, resimleri BGR (Blue, Green, Red) formatinda okur. Ancak, matplotlib görselleştirme için RGB (Red, Green, Blue)
    formatini kullanir. Bu yüzden cv2.cvtColor fonksiyonu ile renk düzeni değiştirilir.
    """

    # Ortalama bulanıklaştırma uygula
    dst2 = cv2.blur(img_rgb, ksize=(3, 3))

    """
    Ortalama Bulaniklaştirma: Bu işlemde, her pikselin değeri çevresindeki piksellerin ortalamasi ile değiştirilir. ksize=(3, 3) parametresi, 
    3x3 boyutunda bir pencere kullanildiğini belirtir.
    """

    # Orijinal resim için ilk pencereyi oluştur
    fig1 = plt.figure()
    plt.imshow(img_rgb)
    plt.axis("off")
    plt.title("Orijinal")
    

    # Bulanıklaştırılmış resim için ikinci pencereyi oluştur
    fig2 = plt.figure()
    plt.imshow(dst2)
    plt.axis("off")
    plt.title("Ortalama Blur")
    

    # gaussian blur
    gb = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=7)
    plt.figure()
    plt.imshow(gb)
    plt.axis("off")
    plt.title("Gauss Blur")

    """
    Gaussian Bulaniklaştirma: Bu bulaniklaştirma, piksellerin ağirlikli ortalamasi ile yapilir. Ağirliklar, 
    bir Gauss fonksiyonu (bell curve) kullanilarak belirlenir. sigmaX=7 parametresi, Gaussian fonksiyonunun standart sapmasini belirler.
    """
    

    # medyan blur
    mb = cv2.medianBlur(img, ksize=3)
    plt.figure()
    plt.imshow(mb)
    plt.axis("off")
    plt.title("Medyan Blur")

    """
    Medyan Bulaniklaştirma: Bu işlemde, her pikselin değeri çevresindeki piksellerin medyan değeri ile değiştirilir. 
    Medyan, siralanmiş bir dizinin ortasinda yer alan değeri ifade eder.
    """

    def gaussianNoise(image):
        row, col, ch = image.shape
        mean = 0
        var = 0.05
        sigma = var**0.5

        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss

        return noisy
    
    """
    Gaussian Gürültü: Bu fonksiyon, resme normal dağilima sahip Gaussian gürültüsü ekler. np.random.normal fonksiyonu, 
    belirtilen mean (ortalama) ve sigma (standart sapma) değerleri ile rastgele gürültü üretir.
    image + gauss: Gürültü, orijinal görüntüye eklenir.

    """

    # içe aktar normalize et
    img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Goruntu_Bulaniklastirma\gorseller-6-m.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255
    plt.figure()
    plt.imshow(img)
    plt.axis("off")
    plt.title("Orijinal")
    
    gaussianNoiseimage = gaussianNoise(img)
    plt.figure()
    plt.imshow(gaussianNoiseimage)
    plt.axis("off")
    plt.title("Gauss Noisy")
    
    # gauss blur
    gb2 = cv2.GaussianBlur(gaussianNoiseimage, ksize=(3, 3), sigmaX=7)
    plt.figure()
    plt.imshow(gb2)
    plt.axis("off")
    plt.title("With Gauss Blur")

    """
    matplotlib.pyplot kullanilarak, yapilan her işlemden sonra farkli görüntüler görselleştirilir. 
    imshow fonksiyonu ile görüntü eklenir, axis("off") ile eksenler gizlenir ve her görüntü için bir başlik atanir.
    """

    def saltPepperNoise(image):
        row, col, ch = image.shape
        s_vs_p = 0.3
        amount = 0.004

        noisy = np.copy(image)

        # salt beyaz
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape]
        noisy[coords[0], coords[1], :] = 1

        # pepper siyah
        num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
        coords = [np.random.randint(0, i, int(num_pepper)) for i in image.shape]
        noisy[coords[0], coords[1], :] = 0

        return noisy
    
    """
    Tuz ve Biber (Salt-Pepper) Gürültüsü: Bu tür gürültü, görüntüde bazi pikselleri tamamen siyah (biber) veya 
    beyaz (tuz) yapar. s_vs_p parametresi, tuz ve biber oranini kontrol eder.
    np.random.randint ile rastgele koordinatlar seçilir ve bu koordinatlarda piksellerin değeri değiştirilir.
    """
    
    spImage = saltPepperNoise(img)
    plt.figure()
    plt.imshow(spImage)
    plt.axis("off")
    plt.title("SP Image")

    plt.show()  # Diğer pencereyi de bekle

    """
    plt.show() komutu, tüm görselleştirilmiş görüntülerin gösterilmesini sağlar. Bu komut çağrilana kadar, 
    matplotlib'teki figürler gösterilmez.
    """
