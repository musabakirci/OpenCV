import cv2

# Resmi yükle
img = cv2.imread(r"C:\Users\MUSA\Desktop\OpenCV\Boyutlandirma_Kirpma\Ataturk.jpg")

# Resim başarıyla yüklendi mi kontrol et
if img is None:
    print("Resim yüklenemedi! Dosya yolunu kontrol et.")
   
    """
    img is None: Eğer cv2.imread() fonksiyonu resmi yükleyemezse (örneğin yanlış bir dosya yolu verilirse), img değişkeni None değerini alır.
    Eğer img boşsa (yani resim yüklenememişse), bir hata mesaji veririz.
    """


else:
    print("Resim boyutu: ", img.shape)

    """
    img.shape: Görüntünün boyutlarini döndürür. Bu, görüntünün yüksekliği,
    genişliği ve renk kanallarinin sayisini içerir.
    """

    # Orijinal resmi göster
    cv2.imshow("Orijinal", img)

    """
    cv2.imshow(): Görüntüyü bir pencerede gösterir. Burada "Orijinal" pencere 
    başliğidir ve img resmini ekranda gösterir.
    """

    # Resmi yeniden boyutlandır
    imgResized = cv2.resize(img, (600, 600))
    print("Boyutlandirilan Foto Şekli: ", imgResized.shape)

    """
    cv2.resize(): Görüntüyü yeniden boyutlandirir. Burada resmi 600x600 boyutlarina yeniden ölçeklendiriyoruz.
    imgResized: Yeniden boyutlandirilmiş resmi tutan değişkendir.
    """

    # Boyutlandırılmış resmi göster
    cv2.imshow("Foto Boyutu", imgResized)
    
    """
    cv2.imshow(): Yeniden boyutlandirilmiş resmi ekranda göstermek için kullanilir.
    """

    # Kırpma işlemi
    imCropped = img[:200, :250]  # İlk 50 satır, ilk 100 sütun
    print("Kirpilmiş Resim Boyutu: ", imCropped.shape)

    """
    img[:50, :100]: İlk 50 satir ve ilk 100 sütunu seçer. Yani 50x100 boyutunda bir bölgeyi kirpar.
    imCropped: Kirpilmiş görüntüyü tutan değişkendir.
    """

    # Kırpılmış resmi göster
    cv2.imshow("Kirpilmiş Resim", imCropped)

    """
    cv2.imshow(): Kirpilmiş resmi ekranda gösterir.
    """

    # Pencerelerin açık kalmasını sağla
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

    """
    cv2.waitKey(0): Bir tuşa basilana kadar bekler. Bu, görüntü penceresinin açik kalmasini sağlar.
    cv2.destroyAllWindows(): Tüm OpenCV pencerelerini kapatir. Bir tuşa basildiğinda tüm pencereler kapanir.
    """
    
    """
    Resim yüklenir.
    Orijinal resim gösterilir.
    Resim yeniden boyutlandirilir ve gösterilir.
    Resim kirpilir ve gösterilir.
    Son olarak, bir tuşa basana kadar pencereler açik kalir.
    """
