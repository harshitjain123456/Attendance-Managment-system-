import cv2
import numpy as np
import face_recognition
from tkinter import *
import os
from datetime import datetime

class Attendence:
    def __init__(self, root):
        path='imagesface'
        images=[]
        classNames=[]
        myList=os.listdir(path)
        print(myList)
        for cl in myList:
            curimg=cv2.imread(f'{path}/{cl}')
            classNames.append(os.path.splitext(cl)[0])
            images.append(curimg)
        print(classNames)

        def findEncodings(images):
            encodelist=[]
            for img in images:
                img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                encode=face_recognition.face_encodings(img)[0]
                encodelist.append(encode)
            return encodelist
        def markattendence(name):
            with open('attendence.csv','r+') as f:
                mydatalist=f.readlines()
                namelist=[]
                for line in mydatalist:
                    entry=line.split(',')
                    namelist.append(entry[0])
                if name not in namelist:
                    now=datetime.now()
                    dstring=now.strftime('%m/%d/%Y')
                    dtimes=now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dstring},{dtimes}')

        encodeListKnown=findEncodings(images)
        print(len(encodeListKnown))

        cap=cv2.VideoCapture(0)

        while True:
            success,img=cap.read()
            imgs=cv2.resize(img,(0,0),None,0.25,0.25)
            imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

            facescurframe=face_recognition.face_locations(imgs)
            encodescurframe = face_recognition.face_encodings(imgs,facescurframe)
            for encodeFace,faceloc in zip(encodescurframe,facescurframe):
                matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
                facedis=face_recognition.face_distance(encodeListKnown,encodeFace)
                print(facedis)
                matchindex=np.argmin(facedis)

                if matches[matchindex]:
                    name=classNames[matchindex].upper()
                    print(name)
                    y1,x2,y2,x1=faceloc
                    y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    markattendence(name)


            cv2.imshow('webcam',img)
            cv2.waitKey(1)
            key_pressed=cv2.waitKey(1) & 0XFF
            if key_pressed==ord('q'):
                break

        cv2.destroyAllWindows()

if __name__=="__main__":
    root = Tk()
    ob = Attendence(root)
    root.mainloop()