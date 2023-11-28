  // Import the functions you need from the SDKs you need
 import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
 import { getDatabase, ref, set, get, child } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
 const firebaseConfig = {
    apiKey: "AIzaSyBUWXVV963Ca75tyagh4TpIzekvnuDC_vM",
    authDomain: "studentdetails-8b2ff.firebaseapp.com",
    projectId: "studentdetails-8b2ff",
    storageBucket: "studentdetails-8b2ff.appspot.com",
    messagingSenderId: "242019945419",
    appId: "1:242019945419:web:f675c067b896e34261c44e",
    measurementId: "G-XFCLKG0J56"
  };



firebase.initializeApp(firebaseConfig);

function UploadStudentdata(){
    var fnameInput=document.getElementById("FirstName");
    var FirstName=fnameInput.value;
    var mnameInput=document.getElementById("MiddleName");
    var MiddleName=mnameInput.value;
    var lnameInput=document.getElementById("LastName");
    var LastName=lnameInput.value;
    var erpInput=document.getElementById("ERPNo");
    var ERPNo=erpInput.value;

    var photo=document.getElementById("photo");
    var file=photo.files[0];
    var storageRef=firebase.storage().ref();
    var uploadtask=storageRef.child('photos/'+file.ERPNO).put(file);

    uploadtask.on('state_changed',
        function(snapshot){
            var progress=(snapshot.bytesTransferred/snapshot.totalBytes)*100;
            document.getElementById('uploadProgrss').value=progress;
        },
        function(error){
            document.getElementById('message').innerHTML='UPLOAD FAILES:' + error;
        },
        function(){
            uploadtask.snapshot.ref.getDownloadURL().then(function(downloadURL){
                saveStudentData(ERPNo,downloadURL,FirstName,LastName,MiddleName)
            });
            }
        
    );    
    
}
function saveStudentData(ERPNo,photoURL,FirstName,LastName,MiddleName){
    var databaseRef=firebase.database().ref('studentdetails');
    var newstudentRef=databaseRef.push();
    newstudentRef.set({
        ERPNO: ERPNo,
        FIRSTNAME: FirstName,
        MIDDLENAME: MiddleName,
        LASTNAME: LastName,
        photoURL: photoURL
    })
    .then(function(){
        document.getElementById('message').innerHTML='Student data Uploaded successfully!';
        document.getElementById('ERPNo').value='';
        document.getElementById('FirstName').value='';
        document.getElementById('MiddleName').value='';
        document.getElementById('LastName').value='';
        document.getElementById('photo').value='';
    })
    .catch(function(error){
        document.getElementById('message').innerHTML='Error uploading Student Data:'+error;
    });
}

/*
function validation(){
    if(document.FormFill.FirstName.value==""){
        document.getElementById("result").innerHTML="Enter First Name**";
        return false;
    }
    if(document.FormFill.LastName.value==""){
        document.getElementById("result").innerHTML="Enter Last Name **";
        return false;
    }
    if(document.FormFill.ERPNo.value==""){
        document.getElementById("result").innerHTML="Enter ERP NO. **";
        return false;
    }
    else if(document.FormFill.ERPNo.value==""){
        document.getElementById("result").innerHTML="Please check your ERP No. **";
        return false
    }
    else if(document.FormFill.photo.value!=''){
        popup.classList.add("open-slide")
    }
    else{
        document.getElementById("result").innerHTML="PHOTO NOT UPLOADED **";
        return false;
    }
}
var popup=document.getElementById('popup');
function CloseSlide(){
    popup.classList.remove("open-slide")
} */