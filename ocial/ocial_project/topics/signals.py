from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

import json
from .middlewares import RequestMiddleware
from .models import Topic, ActivityStream_JSON
from datetime import datetime
from django.urls import reverse
import requests


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
    req = requests.post("http://activity_stream:3000/echo", json=activity)
