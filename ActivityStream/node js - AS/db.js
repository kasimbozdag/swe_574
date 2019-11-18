const firebase = require("firebase");
const http = require('http');
const express = require("express");
var fileName = "app.js"
const hostname = '127.0.0.1';
const port = 3000;
class Database{


//var app = express();
	constructor(db, ref, defaultProject){
		// var firebaseConfig = {
		// 		    apiKey: "AIzaSyB1LAB8kTCwczJOzKN7R2cx0m340r4UjUM",
		// 		    authDomain: "activity-85126.firebaseapp.com",
		// 		    databaseURL: "https://activity-85126.firebaseio.com",
		// 		    projectId: "activity-85126",
		// 		    storageBucket: "activity-85126.appspot.com",
		// 		    messagingSenderId: "739852772274",
		// 		    appId: "1:739852772274:web:85f7342f6a4d4eb701faab"
		// 		  };
		  this.defaultProject = defaultProject;
          this.db = db;
          this.ref = db.ref("/activityStreamTest");

	}

	reference(){
		return this.ref;
	}

	getAllActivitiesFromDB(){
		console.log("getAllActivitiesFromDB: working")

		var ref = reference();
		ref.on('value', function(snapshot) {
	    console.log('leadsRef: ');
        snapshot.forEach(function(childSnapshot) {
        var childData = childSnapshot.val();
        console.log(childData);
    });
});
	}




}