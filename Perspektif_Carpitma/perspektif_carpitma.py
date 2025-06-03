import cv2
import numpy as np

# Resmi içe aktar
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Perspektif_Carpitma\perspektif.jpg")

# Resmin yüklendiğini kontrol et
if img is None:
    print("HATA: Resim yüklenemedi! Dosya yolunu kontrol et.")
else:
    cv2.imshow("Orijinal", img)

    """
    Eğer img değişkeni None ise, resmin yüklenemediğini yazdirir ve program çalişmaya devam etmez.
    Eğer resim doğru yüklenmişse, orijinal resmi ekranda gösterir.
    """

    # Yeni genişlik ve yükseklik değerleri
    width = 200
    height = 300

    # Perspektif dönüşümü için noktalar
    pts1 = np.float32([[119,1], [310,302], [414,871], [545,371]])
    pts2 = np.float32([[0,0], [0,height], [width,0], [width,height]])

    """
    pts1: Orijinal resimdeki 4 noktayi tanimlar.
    pts2: Bu noktalarin dönüştürüldükten sonra yerleştirileceği yeni konumlari tanimlar.
    📌 Örnek Açiklama:

    Orijinal resimdeki noktalar (pts1)
    (139,1) → Yeni resimde (0,0) olacak
    (30,302) → Yeni resimde (0,500) olacak
    (34,871) → Yeni resimde (400,0) olacak
    (245,371) → Yeni resimde (400,500) olacak
    Bu noktalar sayesinde perspektif bozulmasini düzelteceğiz.
    """

    # Perspektif dönüşüm matrisini hesapla
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    print("Dönüşüm Matrisi:\n", matrix)

    """
    cv2.getPerspectiveTransform(pts1, pts2), yukarida seçtiğimiz noktalar arasindaki dönüşüm matrisini hesaplar.
    Bu matris, perspektif dönüşümü için gereklidir ve görüntüye uygulanacaktir.
    """

    # Nihai dönüştürülmüş resmi oluştur
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))  

    """
    cv2.warpPerspective() fonksiyonu ile dönüşüm matrisini resme uyguluyoruz.
    Sonuç olarak, perspektifi düzeltilmiş yeni bir görüntü elde ediyoruz.

    """

    # Çıktı resmini göster
    cv2.imshow("Nihai Resim", imgOutput)

    """
    Yeni dönüştürülmüş perspektifi düzeltilmiş resmi ekranda gösterir.
    """

    # Pencerelerin açık kalmasını sağla
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

    """
    cv2.waitKey(0) → Bir tuşa basilana kadar pencerenin açik kalmasini sağlar.
    cv2.destroyAllWindows() → Tüm OpenCV pencerelerini kapatir.
    """


    """
    Resmi yükler ve kontrol eder.
    Perspektif dönüşümü için 4 nokta seçer.
    Dönüşüm matrisini hesaplar.
    cv2.warpPerspective() ile perspektifi düzeltir.
    Yeni perspektif düzeltilmiş görüntüyü gösterir.
    
    🛠 Örnek Durum:
    Eğik bir kağidi ya da kimliği düzgün hale getirmek için kullanilabilir.
    Bir tabelayi düz hale getirmek için kullanabiliriz.
    """