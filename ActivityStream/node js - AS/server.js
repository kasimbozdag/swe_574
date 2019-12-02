//MARK: This files Contains the backend code that is responsible for both GET and POST http requests
var firebase = require("firebase");
const http = require('http');
const url = require('url');
//const databaseF = require('./app.js');
//var name = databaseF.fileName; 

const hostname = '127.0.0.1';
const port = 3000;
var express = require("express");
var app = express();
var serverResponse = {};

var JsonBody = "Response";
var data = {
  responseCode : "0",
  responseDescription : "Activity has been created successfully"
  // type : "Follow"
};
var error = {
  responseCode : "1",
  responseDescription : "Error! please check the correct format of Activity Stream."
  // type : "Follow"
};
var errorWrongEntry = {
  responseCode : "1",
  responseDescription : "Error! wrong entry please check the data that to be queryed "
  // type : "Follow"
};
serverResponse[JsonBody] = [];
serverResponse[JsonBody].push(data);

// MARK: firebase vars
var firebaseConfig = {
    apiKey: "AIzaSyB1LAB8kTCwczJOzKN7R2cx0m340r4UjUM",
    authDomain: "activity-85126.firebaseapp.com",
    databaseURL: "https://activity-85126.firebaseio.com",
    projectId: "activity-85126",
    storageBucket: "activity-85126.appspot.com",
    messagingSenderId: "739852772274",
    appId: "1:739852772274:web:85f7342f6a4d4eb701faab",
  };
//   // Initialize Firebase
 var defaultProject = firebase.initializeApp(firebaseConfig);
  var db = firebase.database();
  var ref = db.ref("/activityStreamTest");

var reference = db.ref('activity-85126');
// getting firebase stored data




const server = http.createServer((request, response) => {
  console.log("The server is running...");
  //console.log(name);
  if (request.method === 'POST' && request.url === '/echo') {
    console.log("Received a post Request!");
    let body = [];
    request.on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
    //  body = Buffer.concat(body).toString();
     var res = JSON.stringify(body);
  //   var res = JSON.stringify(data);
     var jsonObj = JSON.parse(body);
     console.log(jsonObj);
     if(jsonObj.hasOwnProperty('summary') && jsonObj.hasOwnProperty('actor') && jsonObj.hasOwnProperty('type') && jsonObj.hasOwnProperty('object') && jsonObj.hasOwnProperty('published')){
     console.log("=================true");
     console.log("summary:"+jsonObj.summary);
     console.log("actor:"+jsonObj.actor);
     console.log("type:"+jsonObj.type);
     console.log("object:"+jsonObj.object);
     console.log("published:"+jsonObj.published);
     var rerturnedResponse = JSON.stringify(data);

     ref.push(jsonObj);
     response.end(rerturnedResponse);
     }else{// not a stream activity
     var rerturnedResponse = JSON.stringify(error);

     response.end(rerturnedResponse);

     }




     
    });
  }else if (request.method === 'GET' && request.url === '/getAllActivities'){

  console.log("Received a get request");
    // var res = JSON.stringify(data);
    //     response.end(res);
  ref.once("value", function(snapshot) {
  console.log("ref.once ");
  var data = snapshot.val();   //Data is in JSON format.
  var res = JSON.stringify(data);
  response.end(res);

});


  }else if (request.method === "GET" ){
    //  && request.url === '/getActorActivity' 
    console.log("Received a get request for getActorActivity");
    var url_parts = url.parse(request.url,true);
    console.log(url_parts.query);
    var jsonObj = JSON.stringify( url_parts.query );

    console.log("jsonObj"+jsonObj);
    var body = [];
    body.push(jsonObj);
    console.log("body"+body);
    var val = JSON.parse(body);
    console.log("val"+val);


    if (val.hasOwnProperty('actor')){
      console.log("============= has an actor");
      console.log("the actor is: "+val.actor);


      ref.orderByChild("actor").equalTo(val.actor).on("value", function(snapshot) {

      console.log(snapshot.key);
      var data = snapshot.val();   //Data is in JSON format.
      var res = JSON.stringify(data);
      //
    //  var rerturnedResponse = JSON.stringify(data);

     //ref.push(jsonObj);
     response.end(res);
      console.log("json: "+res)

});

    }else{
      // wrong get request
    }
  //  var res = JSON.stringify(request.headers);
   // console.log(res);
    console.log("============= request headers");
   // console.log(request.headers);
    console.log("=============");
    response.writeHead( 200 );
    response.write( JSON.stringify( url_parts.query ) );
    response.end();
    //console.log("HEADERS: ${JSON.stringify(request.headers)}");

  } else {
    response.statusCode = 404;
    response.end();
  }
});


// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World\n');
//    console.log("test");
//    const {header, method, url} = req;
//    let body = [];
//    req.on('error,' (err)=>{
//      console.error(err);

//    }).on('data',(chunk)=>{

//      body.push(chunk);

//    }).on('end',()=>{
//      body = buffer.concat(body).toString();
//    });

//     req.statusCode = 200;
//     req.setHeader('Content-Type', 'application/json');

//     const responseBody = { headers, method, url, body };

//     req.write(JSON.stringify(responseBody));
//     req.end();


// });

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

