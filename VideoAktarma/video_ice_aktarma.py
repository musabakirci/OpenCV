import cv2
import time
"""
cv2 (OpenCV): OpenCV, bilgisayarla görme işlemleri için kullanilan bir kütüphanedir. Bu kodda video işleme ve görselleştirme için kullaniliyor.
time: Videonun oynatma hizini kontrol etmek için bir bekleme fonksiyonu sağlar.
"""

# Video yolu
video_name = r"C:\Users\MUSA\Desktop\OpenCV\videoAktarma\video.mp4"
"""
video_name: Bu değişken, videonun tam dosya yolunu tutar. r harfi (raw string) ters eğik çizgileri kaçiş karakteri olarak işlemekten kurtarir.
"""

# Video içe aktarma: capture, cap
cap = cv2.VideoCapture(video_name)
"""
cv2.VideoCapture: Bu fonksiyon, video dosyasini açmak veya bir kamera kaynağini almak için kullanilir.
video_name: Açilacak video dosyasinin yolunu belirtir.
cap: Video kaynağini temsil eden bir nesnedir.
"""

# Video özellikleri
print("Genişlik: ", cap.get(3))  # Video genişliği
print("Yükseklik: ", cap.get(4))  # Video yüksekliği
"""
cap.get(3): Videonun genişlik bilgisini alir.
cap.get(4): Videonun yükseklik bilgisini alir.
Bu özellikler videonun çözünürlüğünü (örneğin, 1920x1080) belirler.
"""

# Video düzgün açılmış mı kontrol edin
if not cap.isOpened():
    print("Hata: Video açilamadi.")
    exit()
"""
cap.isOpened(): Video dosyasinin başariyla açilip açilmadiğini kontrol eder.
Eğer cap.isOpened() False dönerse, video açilamamiştir ve bir hata mesaji görüntülenir, ardindan program sonlandirilir
"""    

# Video oynatma döngüsü
while True:
    ret, frame = cap.read()
    """
    cap.read(): Video karesini (frame) okur.
    ret: Okuma işleminin başarili olup olmadiğini döner (True veya False).
    frame: Okunan video karesi, bir NumPy dizisi olarak döner.
    Döngü, her bir kareyi sirayla okur.

    Eğer ret == False ise, videonun sonuna gelinmiş demektir ve döngü sonlandirilir.
    """

    if ret:
        time.sleep(0.01)  # Çok hızlı akışı yavaşlatmak için
        cv2.imshow("Video", frame)
  
    else:
        break
    """
    ret == True: Eğer bir kare başariyla okunmuşsa:
    time.sleep(0.01): Videoyu daha doğal bir hizda oynatmak için küçük bir bekleme süresi ekler.
    cv2.imshow(): Okunan kareyi bir pencere içerisinde görüntüler.
    """
    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    """
    cv2.waitKey(1): Her kareyi göstermek için bekler ve klavye girişini kontrol eder.
    ord("q"): Eğer kullanici "q" tuşuna basarsa döngü sonlandirilir.
    """

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
"""
cap.release(): Video dosyasini veya kamerayi serbest birakir.
cv2.destroyAllWindows(): Açik olan tüm OpenCV pencerelerini kapatir.
"""


"""
Özetle:
Video dosyasini belirtilen yoldan açar.
Videonun genişlik ve yükseklik bilgilerini yazdirir.
Her bir kareyi sirayla okur ve bir pencere içinde gösterir.
Kullanici "q" tuşuna basana kadar veya video bitene kadar oynatmaya devam eder.
Kaynaklari serbest birakir ve programi düzgün bir şekilde kapatir.
"""