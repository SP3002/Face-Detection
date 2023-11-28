import cv2
import numpy as np
import face_recognition as faceRegLib
import pickle
import os
import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://nirikshan-e8e13-default-rtdb.firebaseio.com/",
    'storageBucket':"nirikshan-e8e13.appspot.com"
})


#importing photos of students
Folder_Path = "Photo"
path_img_list = os.listdir(Folder_Path)

Img_List = []
Student_Id = []

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

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        mydatalist=f.readlines()
        nameList=[]
        for line in mydatalist:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

print("Encoding started.....")
knwnEncode_List=Find_Encoding(Img_List)
print("Encoding Completed !!..")


knwn_Encode_List_with_id=[knwnEncode_List,Student_Id]

file=open("EncodeFile.p",'wb')
pickle.dump(knwn_Encode_List_with_id,file)
file.close()
print("file saved")

