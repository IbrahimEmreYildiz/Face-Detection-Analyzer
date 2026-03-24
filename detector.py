import cv2


face_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
    )

def detect_faces(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    return faces

def draw_faces(frame, faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
    
    