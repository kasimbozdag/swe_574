var firebase = require("firebase");
const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;
var express = require("express");
var app = express();
// firebase.initializeApp({
//     apiKey: "AIzaSyB1LAB8kTCwczJOzKN7R2cx0m340r4UjUM",
//     authDomain: "activity-85126.firebaseapp.com",
//     databaseURL: "https://activity-85126.firebaseio.com",
//     projectId: "activity-85126",
//     storageBucket: "activity-85126.appspot.com",
//     messagingSenderId: "739852772274",
//     appId: "1:739852772274:web:85f7342f6a4d4eb701faab"
//   });
// var db = firebase.database();
// console.log("Server running at Port 3000");
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
//   ref.set([{
//   "@context": "https://www.w3.org/ns/activitystreams",
//   "type": "Object",
//   "contentMap": {
//     "en": "basr",
//     "fr": "foso"
//   },
//   "name": "mdo",
//   "published": "2019-11-11T06:14:46Z"
// }]);

//   ref.push({
//   "@context": "https://www.w3.org/ns/activitystreams",
//   "type": "Object",
//   "contentMap": {
//     "en": "test",
//     "fr": "as"
//   },
//   "name": "mdo",
//   "published": "2019-11-11T06:14:46Z"
// });
var reference = db.ref('activity-85126');
// getting firebase stored data
ref.once("value", function(snapshot) {
  console.log("ref.once ");
  var data = snapshot.val();   //Data is in JSON format.
  console.log(data);
});
// getting firebase stored data
var leadsRef = db.ref('activity-85126');
leadsRef.on('value', function(snapshot) {
	console.log('leadsRef: ');
    snapshot.forEach(function(childSnapshot) {
      var childData = childSnapshot.val();
      console.log(childData);
    });
});




const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World\n');
   console.log("test");
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});




const as = require('activitystrea.ms');
// const database = firebase.database();
// var defaultProject = firebase.initializeApp(firebaseConfig);

//console.log(defaultProject.name);
// Create a simple object
// {
//   "@context": "https://www.w3.org/ns/activitystreams",
//   "type": "Object",
//   "contentMap": {
//     "en": "bar",
//     "fr": "foo"
//   },
//   "name": "baz",
//   "published": "2019-11-11T06:14:46Z"
// }
as.object().
  name('baz').
  content(
    as.langmap()
      .set('en', 'bar')
      .set('fr', 'foo')).
  publishedNow().
  prettyWrite((err,doc) => {
    if (err) throw err;
  //  console.log(doc);
   // database.set(doc);
  });

  //{
//   "@context": [
//      "https://www.w3.org/ns/activitystreams",
//      {
//       "css": "http://www.w3.org/ns/oa#styledBy"
//      }
//   ],
//   "summary": "A note",
//   "type": "Note",
//   "content": "My dog has fleas.",
//   "css": "http://www.csszengarden.com/217/217.css?v=8may2013"
// }
// getting firebase stored data
console.log("-----------------------------------------------");
ref.on("child_added", function(snapshot, prevChildKey) {
  console.log("firebase database");
  console.log("-----------------------------------------------");
  var newActivity = snapshot.val();
 // console.log("newActivity" + newActivity.val());
  console.log("context: " + newActivity.context);
  console.log("type: " + newActivity.type);
  console.log("Previous Post ID: " + prevChildKey);
  console.log("summary: "+ newActivity.summary);
  console.log("actor type: "+ newActivity.actor);
  console.log("published: "+ newActivity.published);
//   snapshot.forEach(function(snapshot2) {
//       console.log(childSnapshot.key); }
//   // var objectId =  newActivity.object.val();
//   // console.log("object: "+ objectId.id);


});
console.log("-----------------------------------------------");

var obj = {
  '@context': 'https://www.w3.org/ns/activitystreams',
  '@type': 'Person',
  name: 'Joe'
};
as.import(obj, (err, imp) => {
  if (err) throw err;
  console.log(imp.type);
 // database.set(imp.type)
  //console.log(obj);
 // console.log(imp);

});
//as.stream();

// var admin = require("firebase-admin");

// // Get a database reference to our posts
// var db = admin.database();
// var ref = db.ref("activity-85126");

// Attach an asynchronous callback to read the data at our posts reference
// ref.on("value", function(snapshot) {
//   console.log("firebase data:");
//   console.log(snapshot.val());
// }, function (errorObject) {
//   console.log("The read failed: " + errorObject.code);
// });

