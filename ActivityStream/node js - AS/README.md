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
### Sending a get request using postman for retrieving activity stream based on 'TYPE':

once your server is running type http://127.0.0.1:3000/getAllActivities?type=create for http address, and for http method select a get then click send then the response would be as following:

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
    "-Lv5FNIKpNI16zx69kQ0": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://example/kasim",
        "object": "http://example.com/courseId57",
        "published": "2015-02-10T15:04:55Z",
        "summary": "kasim created a new learning path with title body language",
        "type": "create"
    },
    "-LvaTV5NHeKG7pq1VVBI": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://127.0.0.1:8002/kasim2/",
        "object": "http://127.0.0.1:8002/exploretopic/6",
        "published": "2019-12-08T17:06:25Z",
        "summary": "The User kasim2 added the topic 'testtest'",
        "type": "create"
    },
    "-LvaZARnS3GqTzOSir-6": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://127.0.0.1:8002/kasim2/",
        "object": [
            "http://127.0.0.1:8002/exploretopic/7"
        ],
        "published": "2019-12-08T17:31:14Z",
        "summary": "The User kasim2 added the topic 'test2'",
        "type": "create"
    },
    "-LvdpCMWa8nyFm0WF_gt": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://18.220.59.96:8002/Kaanaydin/",
        "object": [
            "http://18.220.59.96:8002/exploretopic/14"
        ],
        "published": "2019-12-09T08:44:30Z",
        "summary": "The User Kaanaydin added the topic 'Autonomous Vehicles'",
        "type": "create"
    }
}
```
### Sending a get request using postman for retrieving activity stream based on 'object':

once your server is running type http://127.0.0.1:3000/getAllActivities?object=http://127.0.0.1:8002/exploretopic/6 for http address, and for http method select a get then click send then the response would be as following:

```
{
    "-LvaTV5NHeKG7pq1VVBI": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://127.0.0.1:8002/kasim2/",
        "object": "http://127.0.0.1:8002/exploretopic/6",
        "published": "2019-12-08T17:06:25Z",
        "summary": "The User kasim2 added the topic 'testtest'",
        "type": "create"
    }
}
```
### Sending a get request using postman for retrieving activity stream based on 'published':

once your server is running type http://127.0.0.1:3000/getAllActivities?published=2019-12-08T17:06:25Z for http address, and for http method select a get then click send then the response would be as following:

```
{
    "-LvaTV5NHeKG7pq1VVBI": {
        "@context": "https://www.w3.org/ns/activitystreams",
        "actor": "http://127.0.0.1:8002/kasim2/",
        "object": "http://127.0.0.1:8002/exploretopic/6",
        "published": "2019-12-08T17:06:25Z",
        "summary": "The User kasim2 added the topic 'testtest'",
        "type": "create"
    }
}
```