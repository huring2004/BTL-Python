import os
import cv2
import face_recognition
import pickle

folderPath = "../Backend/Image/"

ModePath = os.listdir(folderPath)
imgList = []
stdIds = []

for i in ModePath:
    imgList.append(cv2.imread(os.path.join(folderPath, i)))
    stdIds.append(os.path.splitext(i)[0])

def findE(igList):
    enList = []
    for i in igList:
        # Convert image from BGR to RGB
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(i)[0]
        enList.append(encode)
    return enList
encode= findE(imgList)
encode2 = [encode,stdIds]
file = open("Mahoa.p","wb")
pickle.dump(encode2,file)
file.close()
