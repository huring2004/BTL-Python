import os
import sys
import pickle
import cvzone
import face_recognition
import cv2
import numpy as np
from face_recognition import face_locations

cap = cv2.VideoCapture(1)
# cap.set(3,1200)
# cap.set(4,800)
folderModePath = "../Backend/resources/Modes/"

ModePath = os.listdir(folderModePath)
imgModeList = [] # matran diem anh
for i in ModePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,i)))


#import file Mahoa

file = open("Mahoa.p","rb")
enList = pickle.load(file)
file.close()
encode,stdIds = enList
print(stdIds)

while True:
    ret,frame = cap.read()
    imgS = cv2.resize(frame,(0,0),None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceFrame = face_recognition.face_locations(imgS)
    encodeFrame = face_recognition.face_encodings(imgS,faceFrame)

    for e,f in zip(encodeFrame,faceFrame):
        mat = face_recognition.compare_faces(encode,e)
        faceDis = face_recognition.face_distance(encode,e)
        matIdx = np.argmin(faceDis) # chỉ số của thằng ảnh nhỏ nhất
        if mat[matIdx]:
            y1, x2, y2, x1 = f
            y1, x2, y2, x1 = y1*4, x2*4, y2*4,x1*4
            bbox = x1,y1,x2-x1,y2-y1
            frame = cvzone.cornerRect(frame,bbox, rt = 0)

    cv2.imshow("test", frame)
    if cv2.waitKey(1) == ord(" "): break

cap.release()
cv2.destroyAllWindows()