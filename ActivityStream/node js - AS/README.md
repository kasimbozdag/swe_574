[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kasimbozdag/swe_574.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kasimbozdag/swe_574/context:python)

# SWE574

## How to run Activity Stream server 

### Local

Open the project(streamActivity/swe_574/ActivityStream/node\ js\ -\ AS) at your terminal

then type in your terminal: node server.js

the server should be running now at : http://127.0.0.1:3000/ of your local machine other wise the terminal would notify you for needed node js framework to be installed 

### in order to check whether node js is installed or not type in your terminal:
node -v
 if you do not have node js installed Go to nodejs.org. You'll see download links for MacOS.
 or type in your terminal: npm install

### Sending a get request using postman

once your server is running type http://127.0.0.1:3000/getAllActivities for http address, and for http method select a get then click send

Add SECRET_KEY to the local_settings.py

Add database settings to local_settings.py

Example code for JSON ld for get request

```
{
    "-Lv1p3L2E2pR7poBug3E": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://example/mahmutAoata",
        "object": "http://example.com/courseId4",
        "published": "2015-02-10T15:04:55Z",
        "summary": "mahmoud created a new topic",
        "type": "create"
    },
    "-Lv1pEzU56gTuD004WOy": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://example/emre",
        "object": "http://example.com/courseId34",
        "published": "2015-02-10T15:04:55Z",
        "summary": "emre followed a new topic",
        "type": "create"
    },
    "-Lv1q2N7SXFyP9iSQeR2": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://example/kasim",
        "object": "http://example.com/courseId324",
        "published": "2015-02-10T15:04:55Z",
        "summary": "kasim updated muscle car to be  cars for breaking through mountains  ",
        "type": "update"
    }
}
```
### Sending a post request using postman
once your server is running type http://127.0.0.1:3000/echo for http address, and for http method select a post then for the post request's body should be as follwing then click send:


```
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "summary": "kasim updated muscle car to be  cars for breaking through mountains  ",
  "type": "update",
  "actor": "http://example/userprofile/kasim",
  "object": "http://example.com/courseId324",
  "published" : "2015-02-10T15:04:55Z"
}
```
or 


```
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "summary": "kasim followed a healthy food topic ",
  "type": "follow",
  "actor": "http://example/userprofile/kasim",
  "object": "http://example.com/courseId324",
  "published" : "2015-02-10T15:04:55Z"
}
```
or
```
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "summary": "kasim followed a healthy food topic ",
  "type": "unfollow",
  "actor": "http://example/userprofile/kasim",
  "object": "http://example.com/courseId324",
  "published" : "2015-02-10T15:04:55Z"
}
```
or

```
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "summary": "kasim enroll a healthy food topic ",
  "type": "enroll",
  "actor": "http://example/userprofile/kasim",
  "object": "http://example.com/courseId324",
  "published" : "2015-02-10T15:04:55Z"
}
```
or 
```
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "summary": "kasim finish learning for a healthy food topic ",
  "type": "finish",
  "actor": "http://example/userprofile/kasim",
  "object": "http://example.com/courseId32s4",
  "published" : "2015-02-10T15:04:55Z"
}
```
