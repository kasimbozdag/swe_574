from django.test import TestCase
from topics.models import *
from django.utils import timezone
import pytz
import requests
import json
import hashlib
from datetime import datetime

class TopicTestCase(TestCase):

	def setUp(self):

		self.topic = Topic.objects.create(
		  title='Sport',
		)


	def test_get_title(self):

		topic = Topic.objects.get(title="Sport")
		self.assertEqual(topic.title, 'Sport')


class CourseTestCase(TestCase):

	def setUp(self):

		self.topic = Topic.objects.create(
		  title='Sport'
		)

		self.pubdate = timezone.now()

		self.teacher = User.objects.create_user(
			username = 'test_user',
			password = 'testtest',
			email = 'test@test.com'
		)

		self.course = Course.objects.create(
		  title='American Football',
		  description = 'Americas most popular sport',
		  topic = self.topic,
		  pubdate = self.pubdate,
		  teacher = self.teacher
		)


	def test_course_title(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.title, 'American Football')

	def test_course_topic_title(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.topic.title, 'Sport')

	def test_course_teacher(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.teacher.username, 'test_user')

	def test_course_published(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.published, 0)

	def test_course_isPublishable(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.isPublishable, 0)


	def test_course_completeRate(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.completeRate, 0)

	def test_course_numberofLearners(self):
		course = Course.objects.get(title="American Football")
		self.assertEqual(course.numberofLearners, 0)

class GlossaryTestCase(TestCase):

	def setUp(self):

		self.topic = Topic.objects.create(
		  title='Sport',
		)

		self.pubdate = timezone.now()

		self.teacher = User.objects.create_user(
			username = 'test_user',
			password = 'testtest',
			email = 'test@test.com'
		)

		self.course = Course.objects.create(
		  title='American Football',
		  description = 'Americas most popular sport',
		  topic = self.topic,
		  pubdate = self.pubdate,
		  teacher = self.teacher
		)

		API_ENDPOINT = "https://www.wikidata.org/w/api.php"
		wiki_id = "Q42"
		query =  wiki_id
		params = {
				'action': 'wbsearchentities',
				'format': 'json',
				'language': 'en',
				'limit': '1',
				'search': query
			}
		wiki_request = requests.get(API_ENDPOINT, params = params)
		r_json = wiki_request.json()['search']
		r_json = json.dumps(r_json)
		r_json = json.loads(r_json)

		for entity in r_json:
			self.name = entity['label']
			self.description = entity['description']
			self.url = "https:" + entity['url']

		self.glossary = Glossary.objects.create(name=self.name,description=self.description,url=self.url, course=self.course)

	def test_glossary_name(self):

		glossary = Glossary.objects.get(name="Douglas Adams")
		self.assertEqual(glossary.name, 'Douglas Adams')


	def test_glossary_description(self):

		glossary = Glossary.objects.get(name="Douglas Adams")
		self.assertEqual(glossary.description, 'English writer and humorist')


	def test_glossary_url(self):

		glossary = Glossary.objects.get(name="Douglas Adams")
		self.assertEqual(glossary.url, 'https://www.wikidata.org/wiki/Q42')


class ActivityStream_JSONTestCase(TestCase):
	def setUp(self):
		self.summary = "test_case"


	def test_check_validity(self):
		test = ActivityStream_JSON()
		self.assertEqual(test.check_validity({
					"@context": "https://www.w3.org/ns/activitystreams",
					"summary": "testUser1 created new testCourse",
					"type": "create",
					"actor": "testUser1",
					"object": "testCourse",
					"published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
				}),True)


	def test_get_object(self):
		self.assertEqual(self.summary, "test_case")

class GetActivityStreamTestCase(TestCase):



	def test_getFollowedActivities(self):
		user_test2 = User.objects.create_user(
	   		username = 'test__user',
	    	password = 'testtest',
	    	email = 'test@test.com'
	    )
		user_test = User.objects.create_user(
   			username = 'test___user',
	   		password = 'testtest',
	   		email = 'test@test.com'
	   	)

		self.assertEqual(user_test2.username, "test__user")
