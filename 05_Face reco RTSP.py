import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
import time
import pyrebase

# --------------------------------------   Firebase Initialization -----------------------------------------------------
firebaseConfig = {
  "apiKey": "AIzaSyBXd2DWvsLX8xujmCCDz6DVYyAoQXtP8mo",
  "authDomain": "attendance-e4731.firebaseapp.com",
  "databaseURL": "https://attendance-e4731-default-rtdb.firebaseio.com",
  "projectId": "attendance-e4731",
  "storageBucket": "attendance-e4731.appspot.com",
  "messagingSenderId": "600042187668",
  "appId": "1:600042187668:web:fc0307a0d1f4c414647d81",
  "measurementId": "G-YEX3H66J3Y"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# ----------------------------------------------------------------------------------------------------------------------


name_lst = []
path = 'res'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def update_firebase(date, name_f, time):
    # data = {"Crowd": {"face count": str(count), "message": "Crowd Detected"}}
    date = str(date)
    name_f = str(name_f)
    time =str(time)
    data = {name_f: time}
    db.child(date).update(data)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList





def markAttendance(Name):
    print("\n\nGETTING LIST OF EMPLOYEES PRESENT TODAY")
    now = datetime.now()
    time_String = now.strftime('%H:%M')
    date_String = now.strftime("%d-%m-%Y")
    RowCount = 0
    ColCount = 0
    name_c = 0
    a = 0
    f = open('files/01_Attendance.csv', "r+")
    csv_f = csv.reader(f, delimiter=",")
    Name_meeting = " "
    for row in csv_f:
        RowCount = RowCount + 1
        ColCount = 0
        for field in row:
            ColCount = ColCount + 1
            if ColCount == 1:
                Name_meeting = field
            if ColCount == 2 and date_String == field:
                if Name == Name_meeting:
                    a = 1
                name_c = name_c + 1
    if a == 0:
        print("punching not found")
        f.writelines(f'\n{Name},{date_String},{time_String}')
        time.sleep(0.1)
        #update_firebase(date_String, Name, time_String)
        f.close()
    else:
        print("punching found")
    return name_c




encodeListKnown = findEncodings(images)
print('Encoding complete')

cap = cv2.VideoCapture("rtsp://192.168.253.90:8554/mjpeg/1")
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            #name = classNames[matchIndex].upper()
            name = classNames[matchIndex]
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, .5, (255, 255, 255), 1)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
