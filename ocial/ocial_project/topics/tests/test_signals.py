from django.test import TestCase
from topics.models import *
from django.utils import timezone
import pytz
import requests
import json
import hashlib
from datetime import datetime

class TestSignals(TestCase):

    def test_topic_post_save(self):

        summary = f"emre added the topic 'Car'"
        actor = "emre"
        type = "created"
        object = "topic1"
        activity = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": summary,
            "type": type,
            "actor": actor,
            "object": object,
            "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
        }

        self.assertEqual(activity["type"], "created")


    def test_course_post_enrolled_finished(self):

            isFinished = True
            completeRate = 100
            created = False


            if isFinished == False and completeRate <= 0 and created:
                summary = f"emre enrolled to course 'Cars'"
                actor = "emre"
                type = "enroll"
                object = "course1"

            elif isFinished == True and completeRate >= 100:
                summary = f"emre finished the course 'Cars'"
                actor = "emre"
                type = "finish"
                object = "course1"

            activity = {
                "@context": "https://www.w3.org/ns/activitystreams",
                "summary": summary,
                "type": type,
                "actor": actor,
                "object": object,
                "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
            }

            self.assertEqual(activity["type"], "finish")

    def test_following(self):

        created = True

        if created:
            summary = f"emre followed firat"
            actor = "emre"
            type = "follow"
            object = "firat"

        activity = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": summary,
            "type": type,
            "actor": actor,
            "object": object,
            "published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
        }
        self.assertEqual(activity["type"], "follow")
