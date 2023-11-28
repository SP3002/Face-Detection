import cv2
import pickle
import face_recognition
import face_recognition as faceRegLib
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import os
from datetime import datetime
import json


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://nirikshan-e8e13-default-rtdb.firebaseio.com/",
    'storageBucket':"nirikshan-e8e13.appspot.com"
})


#capturing the video
Face_Capture=cv2.CascadeClassifier("C:/Users/micha/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

Video_Capture= cv2.VideoCapture(0)
Video_Capture.set(3,640)   #setting the image
Video_Capture.set(4,480)

Background=cv2.imread("captbg.png")


#importing photos of students
Folder_Path = "Photo"
path_img_list = os.listdir(Folder_Path)

Img_List = []
Student_Id = []
mylist=os.listdir(Folder_Path)
print(mylist)
for path in path_img_list:

    Img_List.append(cv2.imread(os.path.join(Folder_Path,path)))

    #print(os.path.splitext(path)[0])
    Student_Id.append(os.path.splitext(path)[0])

    fileName = os.path.join(Folder_Path,path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


#print(Student_Id)

def Find_Encoding(Img_List):
    Encode_List=[]
    for img in Img_List:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        Encode=faceRegLib.face_encodings(img)[0]
        Encode_List.append(Encode)

    return Encode_List


def markAttendance(ID):
    with open('attendance.csv','r+') as f:
        mydatalist=f.readlines()
        for line in mydatalist:
            entry=line.split(',')
            Student_Id.append(entry[0])
        if ID not in Student_Id:
            curr=datetime.now()
            dtString=curr.strftime('%H:%M:%S')
            f.writelines(f'\n{ID},{dtString}')

print("Encoding started.....")
knwnEncode_List=Find_Encoding(Img_List)
print("Encoding Completed !!..")


knwn_Encode_List_with_id=[knwnEncode_List,Student_Id]

file=open("EncodeFile.p",'wb')
pickle.dump(knwn_Encode_List_with_id,file)
file.close()
print("file saved")



file=open('EncodeFile.p','rb')
knwn_Encode_List_with_id = pickle.load(file)
file.close()
knwnEncode_List,Student_Id=knwn_Encode_List_with_id
#print(Student_Id)



while True :
    ret, Video_Data=Video_Capture.read()

    S_img=cv2.resize(Video_Data, (0,0),None,0.25,0.25)
    S_img=cv2.cvtColor(S_img,cv2.COLOR_BGR2RGB)

    Curr_face=face_recognition.face_locations(S_img)
    Encode_curr_frame=face_recognition.face_encodings(S_img,Curr_face)

    for Encode_Face, Face_Loc in zip(Encode_curr_frame,Curr_face):
       
        matches=face_recognition.compare_faces(knwnEncode_List,Encode_Face)
        face_distance=face_recognition.face_distance(knwnEncode_List,Encode_Face)
       
        #print("matches",matches)
        #print("face distance", face_distance)

        Match_Index=np.argmin(face_distance)
        #print("match index", Match_Index)

        if matches[Match_Index]:
            print("KNOWN FACE DETECTED")
            id=Student_Id[Match_Index]
            print(id)
            y1,x2,y2,x1 = Face_Loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            bbox = 10+x1, 190+y1, x2-x1, y2-y1
            Video_Data = cvzone.cornerRect(Video_Data, bbox, rt=1)
            
            markAttendance(id)

    Background[190:190+480,10:10+640]=Video_Data

    cv2.imshow("NIRIKSHAN", Background)
   
    if cv2.waitKey(1) == ord("e") :
        break

Video_Capture.release()  