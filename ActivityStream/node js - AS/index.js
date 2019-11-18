const database = require("./db.js");
var firebase = require("firebase");
var express = require("express");
const hostname = '127.0.0.1';
const port = 3000;
var express = require("express");
var app = express();


 var firebaseConfig = {
    apiKey: "AIzaSyB1LAB8kTCwczJOzKN7R2cx0m340r4UjUM",
    authDomain: "activity-85126.firebaseapp.com",
    databaseURL: "https://activity-85126.firebaseio.com",
    projectId: "activity-85126",
    storageBucket: "activity-85126.appspot.com",
    messagingSenderId: "739852772274",
    appId: "1:739852772274:web:85f7342f6a4d4eb701faab"
  };

//   // Initialize Firebase

 var defaultProject = firebase.initializeApp(firebaseConfig);
 var db = firebase.database();
 var ref = db.ref("/activityStreamTest");
var db = new Database(db,ref,defaultProject);
db.getAllActivitiesFromDB()
