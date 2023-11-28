import cv2
import face_recognition
import pickle
import os


folderpath='Photo'
modelpathlist = os.listdir(folderpath)
imglist=[]
studentid=[]
for path in modelpathlist:
    imglist.append(cv2.imread(os.path.join(folderpath,path)))
    studentid.append(os.path.splitext(path)[0])

def findencodings(imagelist):
    encodelist=[]
    for img in imagelist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

        return encodelist

print("Encoding started....")    
encodelistknown=findencodings(imglist)
encodelistknownwithids=[encodelistknown, studentid]

print("Encoding Complete!!!")

file=open("Encodedfile.p",'wb')
pickle.dump(encodelistknownwithids,file)
file.close()
print("file saved")