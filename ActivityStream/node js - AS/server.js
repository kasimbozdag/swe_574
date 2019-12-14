//MARK: This files Contains the backend code that is responsible for both GET and POST http requests
var firebase = require("firebase");
const http = require('http');
const url = require('url');
//const Dictionary = require('dictionaryjs');

//const databaseF = require('./app.js');
//var name = databaseF.fileName; 

const hostname = '127.0.0.1';
const port = 3000;
var express = require("express");
var app = express();
var serverResponse = {};
//var dict = new Dictionary();

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
var errorMissingOrWrongEntry = {
  responseCode : "2",
  responseDescription : "Error! Missing or Wrong Entry Please check the properties that have been set."
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
    console.log("Received a get request..");
    var url_parts = url.parse(request.url,true);
    console.log(url_parts.query);
    var jsonObj = JSON.stringify( url_parts.query );

    console.log("jsonObj"+jsonObj);
    var body = [];
    var query = [];
    var queryFlag = 0;
   // var querystatus

    body.push(jsonObj);
    console.log("body"+body);
    var val = JSON.parse(body);
    console.log("val"+val);
    SearchActivityDictionary(val,queryFlag,query,response);

    //check for 
    if (val.hasOwnProperty('published') && val.hasOwnProperty('object') && val.hasOwnProperty('actor')){
      console.log("SearchActivityStream:");
      var value1 = val['published'];
      var value2 = val['object'];
      var value3 = val['actor'];
      SearchActivityStream(val);

    }else if (val.hasOwnProperty('type') && val.hasOwnProperty('object') && val.hasOwnProperty('actor') ){
        // check for actor and object
        console.log('Just Received a get request for type && object and actor');
        ref.once("value").then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      // key will be "ada" the first time and "alan" the second time
      var ID = childSnapshot.key;
      console.log("============ ID");
      console.log(ID);
      console.log("============ ID");
      // childData will be the actual contents of the child
      var childData = childSnapshot.val();
      console.log(childData);
       var i = 0;
      childSnapshot.forEach(function(childSnapshot2) {
      // key will be "ada" the first time and "alan" the second time
      i = i + 1;
      console.log("counter: "+i);

      var key = childSnapshot2.key;
      var value = childSnapshot2.val();

      // console.log("//============//");
      // console.log(key);
      // console.log(value);
 //     console.log("//============//");
      if (key === 'type' && value === val['type']){
        console.log("****");
        console.log(val['type']);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
       if (key === 'object' && value === val['object']){
        console.log("****");
        console.log(val['object']);
        console.log("*****");
        queryFlag = queryFlag + 1;

      } 
       if (key === 'actor' && value === val['actor']){
        console.log("****");
        console.log(val['actor']);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
      console.log("queryFlag");
      console.log(queryFlag);
      if (queryFlag === 3){
          query.push(childData);
          queryFlag = 0;
          console.log(queryFlag);

          console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");

      }

      if(i === 6){
        i = 0;
        queryFlag = 0;

      } 

      // childData will be the actual contents of the child
    //  var childData = childSnapshot.val();
  });
  });
console.log("result====");
console.log(query);
});
// print the result




    }else if (val.hasOwnProperty('type')){ // check for type
      console.log("============= type");

      ref.orderByChild("type").equalTo(val.type).on("value", function(snapshot) {

      console.log(snapshot.key);
      var data = snapshot.val();   //Data is in JSON format.
      var res = JSON.stringify(data);
      //
    //  var rerturnedResponse = JSON.stringify(data);

     //ref.push(jsonObj);
     response.end(res);
     console.log("json: "+res);


    });
  } else if (val.hasOwnProperty('object')){
      console.log("============= object");

      ref.orderByChild("object").equalTo(val.object).on("value", function(snapshot) {

      console.log(snapshot.key);
      var data = snapshot.val();   //Data is in JSON format.
      var res = JSON.stringify(data);
      //
    //  var rerturnedResponse = JSON.stringify(data);

     //ref.push(jsonObj);
     response.end(res);
     console.log("json: "+res);


    });
  }
    // check all data for published
    else if (val.hasOwnProperty('published')){
      console.log("============= published");

      ref.orderByChild("published").startAt(val.published).on("value", function(snapshot) {

      console.log(snapshot.key);
      var data = snapshot.val();   //Data is in JSON format.
      var res = JSON.stringify(data);
      //
    //  var rerturnedResponse = JSON.stringify(data);

     //ref.push(jsonObj);
     response.end(res);
     console.log("json: "+res);


    });
  } else if (val.hasOwnProperty('actor')){
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
    response.statusCode = 404;
    response.end();

    }
  //  var res = JSON.stringify(request.headers);
   // console.log(res);
    console.log("============= 200 running..");
   // console.log(request.headers);
    console.log("=============");
 //   response.writeHead( 200 );
  //  response.write( JSON.stringify( url_parts.query ) );
  //  response.end();
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



//MARK: - SearchActivityStream()

function SearchActivityStream(val1,val2,val3){
  console.log("SearchActivityStream: running..");
  console.log("val1: "+val1);
if (  !val3 || !val2 || !val3 ){
  // 
  console.log("you have an empty value");

}else{
// correct request
console.log("SearchActivityStream: successful request!");
}
}

//MARK: - SEARCH ACTIVITY STREAM BASED ON A DICTIONARY

function SearchActivityDictionary(dict,queryFlag,query,response){

  console.log("Running SearchActivityDictionary.. "+dict);
  var count = Object.keys(dict).length;
  console.log("dict length: "+count);
  var numOfProperties = false;
  var keys = [];
  var Ids = [];
  var finalResult = {};
  if (count === 3) {
      console.log("count: "+count);
  var index = 0;
  for (val in dict) {
    console.log("value: "+dict[val]);
    console.log("key: "+val);
    console.log("===========/========");
    keys[index] = val;
    index++;
  }
console.log("keys: "+keys[0]);
console.log("the key: "+keys[0] +"is for value: "+dict[keys[0]]);



// get data from firebase
        ref.once("value").then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      // key will be "ada" the first time and "alan" the second time
      var ID = childSnapshot.key;
      console.log("============ ID");
      console.log(ID);
      console.log("============ ID");
      // childData will be the actual contents of the child
      var childData = childSnapshot.val();
      console.log(childData);
       var i = 0;
      childSnapshot.forEach(function(childSnapshot2) {
      // key will be "ada" the first time and "alan" the second time
      i = i + 1;
      console.log("counter: "+i);

      var key = childSnapshot2.key;
      var value = childSnapshot2.val();

      // console.log("//============//");
      // console.log(key);
      // console.log(value);
 //     console.log("//============//");
      if (key === keys[0] && value === dict[keys[0]]){
        console.log("****");
        console.log(keys[0]);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
       if (key === keys[1] && value === dict[keys[1]]){
        console.log("****");
        console.log(keys[1]);
        console.log("*****");
        queryFlag = queryFlag + 1;

      } 
       if (key === keys[2] && value === dict[keys[2]]){
        console.log("****");
        console.log(dict[keys[2]]);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
      console.log("queryFlag");
      console.log(queryFlag);
      if (queryFlag === 3){
          query.push(childData);
          queryFlag = 0;
          Ids.push(ID);
          finalResult[ID] = childData;
          console.log(queryFlag);

          console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");

      }

      if(i === 6){
        i = 0;
        queryFlag = 0;

      } 

      // childData will be the actual contents of the child
    //  var childData = childSnapshot.val();
  });
  });
console.log("SearchActivityDictionary: result");
console.log(query);
console.log("SearchActivityDictionary: Ids: "+Ids);
console.log("SearchActivityDictionary: "+finalResult);
var res = JSON.stringify(finalResult);
//response.end(res);
try{

var responseStatus = query.length;
console.log("responseStatus "+responseStatus);
if (responseStatus > 0){
  response.end(res);
  console.log("res success");
}else{
  console.log("empty result");
     var rerturnedResponse = JSON.stringify(errorMissingOrWrongEntry);
     // json output
     response.end(rerturnedResponse);
//errorMissingOrWrongEntry
//response.end(errorMissingOrWrongEntry);
}


}catch(error){
  console.log("error: "+error);
}

//console.log("SearchActivityDictionary: finalResult "+res);


});




}else if (count === 4){
// do the logic behind that
      console.log("count: "+count);
  var index = 0;
  for (val in dict) {
    console.log("value: "+dict[val]);
    console.log("key: "+val);
    console.log("===========/========");
    keys[index] = val;
    index++;
  }
console.log("keys: "+keys[0]);
console.log("the key: "+keys[0] +"is for value: "+dict[keys[0]]);



// get data from firebase
        ref.once("value").then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      // key will be "ada" the first time and "alan" the second time
      var ID = childSnapshot.key;
      console.log("============ ID");
      console.log(ID);
      console.log("============ ID");
      // childData will be the actual contents of the child
      var childData = childSnapshot.val();
      console.log(childData);
       var i = 0;
      childSnapshot.forEach(function(childSnapshot2) {
      // key will be "ada" the first time and "alan" the second time
      i = i + 1;
      console.log("counter: "+i);

      var key = childSnapshot2.key;
      var value = childSnapshot2.val();

      // console.log("//============//");
      // console.log(key);
      // console.log(value);
 //     console.log("//============//");
      if (key === keys[0] && value === dict[keys[0]]){
        console.log("****");
        console.log(keys[0]);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
       if (key === keys[1] && value === dict[keys[1]]){
        console.log("****");
        console.log(keys[1]);
        console.log("*****");
        queryFlag = queryFlag + 1;

      } 
       if (key === keys[2] && value === dict[keys[2]]){
        console.log("****");
        console.log(dict[keys[2]]);
        console.log("****");
        queryFlag = queryFlag + 1;

      }

      if (key === keys[3] && value === dict[keys[3]]){
        console.log("****");
        console.log(dict[keys[3]]);
        console.log("****");
        queryFlag = queryFlag + 1;
      }

      console.log("queryFlag");
      console.log(queryFlag);
      if (queryFlag === count){
          query.push(childData);
          queryFlag = 0;
          Ids.push(ID);
          finalResult[ID] = childData;
          console.log(queryFlag);

          console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");

      }

      if(i === 6){
        i = 0;
        queryFlag = 0;

      } 

      // childData will be the actual contents of the child
    //  var childData = childSnapshot.val();
  });
  });
console.log("SearchActivityDictionary: result");
console.log(query);
console.log("SearchActivityDictionary: Ids: "+Ids);
console.log("SearchActivityDictionary: "+finalResult);
var res = JSON.stringify(finalResult);
//response.end(res);
try{

var responseStatus = query.length;
console.log("responseStatus "+responseStatus);
if (responseStatus > 0){
  response.end(res);
  console.log("res success");
}else{
  console.log("empty result");
     var rerturnedResponse = JSON.stringify(errorMissingOrWrongEntry);
     // json output
     response.end(rerturnedResponse);
//errorMissingOrWrongEntry
//response.end(errorMissingOrWrongEntry);
}


}catch(error){
  console.log("error: "+error);
}

//console.log("SearchActivityDictionary: finalResult "+res);


});







}else if (count === 2){
        console.log("count: "+count);
  var index = 0;
  for (val in dict) {
    console.log("value: "+dict[val]);
    console.log("key: "+val);
    console.log("===========/========");
    keys[index] = val;
    index++;
  }
console.log("keys: "+keys[0]);
console.log("the key: "+keys[0] +"is for value: "+dict[keys[0]]);



// get data from firebase
        ref.once("value").then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      // key will be "ada" the first time and "alan" the second time
      var ID = childSnapshot.key;
      console.log("============ ID");
      console.log(ID);
      console.log("============ ID");
      // childData will be the actual contents of the child
      var childData = childSnapshot.val();
      console.log(childData);
       var i = 0;
      childSnapshot.forEach(function(childSnapshot2) {
      // key will be "ada" the first time and "alan" the second time
      i = i + 1;
      console.log("counter: "+i);

      var key = childSnapshot2.key;
      var value = childSnapshot2.val();

      // console.log("//============//");
      // console.log(key);
      // console.log(value);
 //     console.log("//============//");
      if (key === keys[0] && value === dict[keys[0]]){
        console.log("****");
        console.log(keys[0]);
        console.log("****");
        queryFlag = queryFlag + 1;

      }
       if (key === keys[1] && value === dict[keys[1]]){
        console.log("****");
        console.log(keys[1]);
        console.log("*****");
        queryFlag = queryFlag + 1;

      } 

      console.log("queryFlag");
      console.log(queryFlag);
      if (queryFlag === count){
          query.push(childData);
          queryFlag = 0;
          Ids.push(ID);
          finalResult[ID] = childData;
          console.log(queryFlag);

          console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");

      }

      if(i === 6){
        i = 0;
        queryFlag = 0;

      } 

      // childData will be the actual contents of the child
    //  var childData = childSnapshot.val();
  });
  });
console.log("SearchActivityDictionary: result");
console.log(query);
console.log("SearchActivityDictionary: Ids: "+Ids);
console.log("SearchActivityDictionary: "+finalResult);
var res = JSON.stringify(finalResult);
//response.end(res);
try{

var responseStatus = query.length;
console.log("responseStatus "+responseStatus);
if (responseStatus > 0){
  response.end(res);
  console.log("res success");
}else{
  console.log("empty result");
     var rerturnedResponse = JSON.stringify(errorMissingOrWrongEntry);
     // json output
     response.end(rerturnedResponse);
//errorMissingOrWrongEntry
//response.end(errorMissingOrWrongEntry);
}


}catch(error){
  console.log("error: "+error);
}

//console.log("SearchActivityDictionary: finalResult "+res);


});

}

 //var dict2 =  Dictionary.set(dict);
// dict2.forEach(function(key,value){
//   console.log("key: "+key);
//   console.log("value: "+ value);

//   next();
// });



}

