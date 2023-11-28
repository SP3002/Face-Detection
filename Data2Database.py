import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://nirikshan-e8e13-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data = {
    "1024":
    {
        "Name" : "SAURABH PATIL",
        "Course" : "MCA" ,
        "Starting year" : 2022
    },
    "1022":
    {
        "Name" : "Narendra Modi",
        "Course" : "Politician",
        "Starting year" : 2014
    },
    "1023":
    {
        "Name" : "Rahul Gandhi",
        "Course" : "Politician",
        "Starting year" : 2019
    },
    "1025":
    {
        "Name" : "Vin Diesel",
        "Course" : "Actor",
        "Starting year" : 2014
    },
    "1026":
    {
        "Name" : "Yogi Adityanath",
        "Course" : "Politician",
        "Starting year" : 2020
    },
    "1027":
    {
        "Name" : "Tejaswini Ingale",
        "Course" : "MCA",
        "Starting year" : 2022
    }
}

for key,value in data.items():
    ref.child(key).set(value)