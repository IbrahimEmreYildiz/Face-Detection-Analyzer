import cv2
from datetime import datetime,timedelta
from data import save_data
from analyzer import analyze_data
from detector import detect_faces, draw_faces


cap=cv2.VideoCapture(0) # Kamerayı açma kodu
son_kayit=datetime.now()
while True: # Burada bir döngü yapılmış kameranın açık olup olmadığına dair kontrol döngüsü
    ret,frame=cap.read() # Burada ret kamera okuması başarılı mı onu sorgular True False olarak
     # frame ise o anki görüntü karesi yani bir numpy array

    if not ret: #ret False ise yani kamera okuması başarısızsa kamera açılmadı diye uyarı geçer ve döngü biter
        print("Kamera açilamadi")
        break
    faces= detect_faces(frame)
    draw_faces(frame,faces)
    face_count= len(faces)
    
    if datetime.now()- son_kayit>= timedelta(seconds=1):
        save_data(face_count)
        son_kayit=datetime.now()
    

    cv2.imshow("Kamera",frame) #Bu da o anki görüntü karelerini göstermek için kullanılan bir komut
# Burada "Kamera" o anki pencerenin başlığı
    if  cv2.waitKey(1) & 0xFF==ord('q'): # Burada bizim klavyeye basıp basmadığımızı kontrol etmek için
        # 1ms durup kontrol edip devam ediyor waitKey kullanmamızın sebebi programın durmadan devam etmesini sağlamak için yoksa input
        #kullanırdık
        break

cap.release() # Kamerayı serbest bırakır.
cv2.destroyAllWindows() # Açık tüm  pencereleri kapatır
analyze_data()


