from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

import json
from .middlewares import RequestMiddleware
from .models import Topic, ActivityStream_JSON, Learner_Course_Record, UserFollowing, Section, Course
from datetime import datetime
from django.urls import reverse
import requests

#activityHost = "http://activity_stream:3000/echo"
activityHost = "http://127.0.0.1:3000/echo"
# this is a signal that will trigger when a Topic instance is saved to db
# if there are other time you want to call functions you can use pre_save, pre_delete, post_delete as argument insteaad of post_ssave
@receiver(post_save, sender=Topic)
def topic_post_save(sender, instance, **kwargs):
    obj = instance
    scheme_host = None
    request = RequestMiddleware(get_response=None)
    if "current_request" in request.thread_local.__dict__:
        request = request.thread_local.current_request
        user = request.user
        scheme_host = request._current_scheme_host
        if user.is_anonymous:
            actor = None
        else:
            actor = scheme_host + reverse("userprofile", kwargs={"username": user.username})
    else:
        actor = None
    object = scheme_host + "/exploretopic/" + str(obj.id)
    type = "create"
    summary = f"The User {user.username} added the topic '{obj.title}'"
    """
    # this part is not necessary for Topic since topic does not have an update

    # the fallowing endpoint with query has not been implemented
    check=requests.get(f"http://activity_stream:3000/getAllActivities?object={object}&type=create")
    try:
        if check.json()=="null":
            type="update"
            summary= f"The User {user.username} updated the topic '{obj.title}'"
    except:
        pass

"""
    activity = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary": summary,
        "type": type,
        "actor": actor,
        "object": object,
        "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
    }
    print(activity)
    req = requests.post(activityHost, json=activity)


@receiver(post_save, sender=Learner_Course_Record)
def course_post_enrolled_finished(sender, instance, created, **kwargs):
        obj = instance
        scheme_host = None
        request = RequestMiddleware(get_response=None)
        if created:
            request = request.thread_local.current_request
            user = request.user
            scheme_host = request._current_scheme_host
            if user.is_anonymous:
                actor = None
            else:
                actor =scheme_host+ reverse("userprofile",kwargs={"username":user.username})
        else:
            actor = None
        if obj.isFinished == False and obj.completeRate <= 0:
            object=scheme_host + "/exploretopic/" + str(obj.id)
            type = "enroll"
            summary = f"The User {user.username} enrolled in the course '{obj.title}'"
            activity = {
                "@context": "https://www.w3.org/ns/activitystreams",
                "summary":summary,
                "type": type,
                "actor": actor,
                "object": object,
                "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
                }
            req=requests.post("http://activity_stream:3000/echo",json=activity)

        if obj.isFinished == True and obj.completeRate >= 100:
            object=scheme_host + "/exploretopic/" + str(obj.id)
            type = "completed"
            summary = f"The User {user.username} completed the course '{obj.title}'"
            activity = {
                "@context": "https://www.w3.org/ns/activitystreams",
                "summary":summary,
                "type": type,
                "actor": actor,
                "object": object,
                "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
                }
            req=requests.post(activityHost,json=activity)

@receiver(post_save, sender=UserFollowing)
def following(sender, instance, **kwargs):
    obj = instance
    scheme_host = None
    request = RequestMiddleware(get_response=None)
    if "current_request" in request.thread_local.__dict__:
        request = request.thread_local.current_request
        user = request.user
        scheme_host = request._current_scheme_host
        if user.is_anonymous:
            actor = None
        else:
            actor =scheme_host+ reverse("userprofile",kwargs={"username":obj.following.username})
    else:
        actor = None
    object=scheme_host + "/" + str(obj.following.username)
    type = "follow"
    summary = f"The User {user.username} has followed you'"
    activity = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary":summary,
        "type": type,
        "actor": actor,
        "object": object,
        "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
        }
    req=requests.post(activityHost,json=activity)

@receiver(post_save, sender=Section)
def sectionCreated(sender, instance, created, **kwargs):
    obj = instance
    scheme_host = None
    request = RequestMiddleware(get_response=None)
    if "current_request" in request.thread_local.__dict__:
        request = request.thread_local.current_request
        user = request.user
        scheme_host = request._current_scheme_host
        if user.is_anonymous:
            actor = None
        else:
            actor =scheme_host+ reverse("userprofile",kwargs={"username":user.username})
    else:
        actor = None
    object=scheme_host + "/exploretopic/" + str(obj.id)
    type = "created"
    summary = f"The User {user.username} created new section to course '{obj.name}'"
    activity = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary":summary,
        "type": type,
        "actor": actor,
        "object": object,
        "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
    }
    if created:
        req=requests.post(activityHost,json=activity)

@receiver(post_save, sender=Course)
def courseCreated(sender, instance, created, **kwargs):
    obj = instance
    scheme_host = None
    request = RequestMiddleware(get_response=None)
    if "current_request" in request.thread_local.__dict__:
        request = request.thread_local.current_request
        user = request.user
        scheme_host = request._current_scheme_host
        if user.is_anonymous:
            actor = None
        else:
            actor =scheme_host+ reverse("userprofile",kwargs={"username":user.username})
    else:
        actor = None
    object=scheme_host + "/exploretopic/" + str(obj.id)
    type = "created"
    summary = f"The User {user.username} created new course to course '{obj.title}'"
    activity = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary":summary,
        "type": type,
        "actor": actor,
        "object": object,
        "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
    }
    if created:
        req=requests.post(activityHost,json=activity)
