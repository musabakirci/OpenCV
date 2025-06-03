import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)
"""
cv2.VideoCapture(0) ile varsayilan web kamerasini açiyoruz.
0, sistemdeki ilk (birincil) kamerayi ifade eder. Eğer başka 
bir kamera bağladiysan 1, 2 gibi değerler deneyebilirsin.
"""

# Kamera açıldı mı kontrol et
if not cap.isOpened():
    print("Kamera açilamadi!")
    exit()

"""
cap.isOpened() fonksiyonu, kameranin başarili bir şekilde açilip açilmadiğini kontrol eder.
Eğer kamera açilmazsa, "Kamera açilamadi!" mesaji yazdirilir ve exit() komutu ile program sonlandirilir.
"""

# Çözünürlük bilgilerini al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Video çözünürlüğü: {width}x{height}")

"""
cap.get(cv2.CAP_PROP_FRAME_WIDTH) → Videonun genişliğini alir.
cap.get(cv2.CAP_PROP_FRAME_HEIGHT) → Videonun yüksekliğini alir.
print(f"Video çözünürlüğü: {width}x{height}") → Çözünürlüğü ekrana yazdirir.
"""

# Video kaydedici başlat
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Daha uyumlu codec
writer = cv2.VideoWriter("video_kaydi.mp4", fourcc, 20, (width, height))

"""
cv2.VideoWriter_fourcc(*"XVID") → Videoyu sikiştirmak için kullanilan codec (kodlayici) türünü belirler. "XVID" codec'i, .mp4 formati ile daha uyumlu çalişir.
cv2.VideoWriter() → Videoyu dosyaya yazmak için kullanilan fonksiyondur.
"video_kaydi.mp4" → Kaydedilecek dosyanin adi.
fourcc → Belirlenen codec türü.
20 → FPS (Frame Per Second - Saniyedeki kare sayisi).
(width, height) → Videonun boyutlari.
"""

try:
    while True:
        ret, frame = cap.read()

        """
        cap.read() → Kameradan bir kare okur.
        ret → Okuma işlemi başarili olduysa True, başarisiz olduysa False döner.
        frame → Okunan kareyi içerir.
        """

        if not ret:
            print("Kare okunamadi, çikiliyor...")
            break
        
        """
        Eğer ret değeri False olursa, görüntü alinamamiş demektir. Bu durumda
        "Kare okunamadi, çikiliyor..." mesaji yazdirilir ve döngü kirilir (break).
        """

        cv2.imshow("Video", frame)
        
        """
        cv2.imshow("Video", frame) → Alinan kareyi "Video" isimli bir pencerede gösterir.
        """

        # Videoyu kaydet
        writer.write(frame)

        """
        writer.write(frame) → Okunan kareyi video dosyasina ekler.
        """

        # 'q' tuşuna basıldığında çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        """
        cv2.waitKey(1) → Klavyeden bir tuşa basilmasini bekler (1 ms gecikme ile).
        & 0xFF == ord("q") → Eğer q tuşuna basilirsa, döngüyü kir (break).
        """

except Exception as e:

    print(f"Hata oluştu: {e}")

    """
    Bir hata oluşursa, program çökmek yerine "Hata oluştu: {e}" mesaji ile hata sebebini ekrana yazdirir.
    """

finally:
    # Kaynakları serbest bırak
    cap.release()
    writer.release()
    cv2.destroyAllWindows()

    """
    cap.release() → Kamerayi kapatir.
    riter.release() → Video kaydetmeyi durdurur ve dosyayi kapatir.
    cv2.destroyAllWindows() → Açik tüm OpenCV pencerelerini kapatir.
    """


"""
📌 Sonuç
✅ Kamera açilir ve çözünürlük bilgisi ekrana yazdirilir.
✅ Kamera görüntüsü alinir ve gösterilir.
✅ Video dosyaya kaydedilir (video_kaydi.mp4).
✅ q tuşuna basildiğinda çikiş yapilir.
✅ Hata durumunda program çökmek yerine uyari verir ve güvenli şekilde kapanir.
"""    
