import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getDatabase,ref,set,get,child } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyBgk6QL4TstM0KQ0qzXVRw6wlNudxSnK_Q",
    authDomain: "nirikshan-4e4c8.firebaseapp.com",
    databaseURL: "https://nirikshan-4e4c8-default-rtdb.firebaseio.com",
    projectId: "nirikshan-4e4c8",
    storageBucket: "nirikshan-4e4c8.appspot.com",
    messagingSenderId: "642289521449",
    appId: "1:642289521449:web:87789d593adeca7077dd38",
    measurementId: "G-F4LGQ5ZDVZ"
  };

const app=initializeApp(firebaseConfig);

const db=getDatabase(app);

document.getElementById("btn").addEventListener('click',function(e){
    
    set(ref(db,'user/' + document.getElementById("ERPNo").value),
    {
        ERPNo: document.getElementById("ERPNo").value,
        FirstName: document.getElementById("FirstName").value,
        MiddleName: document.getElementById("MiddleName").value,
        LastName: document.getElementById("LastName").value
    })
    alert("Login Successfull!!")
})
