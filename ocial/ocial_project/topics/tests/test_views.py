from django.test import TestCase
from topics.models import *
from topics.views import *

class ViewTestCase(TestCase):

	def setUp(self):

		self.pubdate = timezone.now()

		self.teacher = User.objects.create_user(
			username = 'test_user',
			password = 'testtest',
			email = 'test@test.com'
		)

		self.topic = Topic.objects.create(title='Sport')

		self.course = Course.objects.create(
		  title='American Football',
		  description = 'Americas most popular sport',
		  topic = self.topic,
		  pubdate = self.pubdate,
		  teacher = self.teacher
		)

		self.section = Section.objects.create(
			name = 'Rules',
			course = self.course
		)

		self.lecture1 = Lecture.objects.create(
			title = 'Game Rules',
			section = self.section,
			order = 1
		)

		self.lecture2 = Lecture.objects.create(
			title = 'Referees',
			section = self.section,
			order = 4
		)

		self.quiz1 = Quiz.objects.create(
			title = 'Game Rules Quiz',
			section = self.section,
			order = 2
		)

		self.quiz2 = Quiz.objects.create(
			title = 'Play Quiz',
			section = self.section,
			order = 3
		)

	def test_createlearningpath(self):
		section = Section.objects.get(name="Rules")
		lecture1 = Lecture.objects.get(title='Game Rules')
		lecture2 = Lecture.objects.get(title='Referees')
		quiz1 = Quiz.objects.get(title='Game Rules Quiz')
		quiz2 = Quiz.objects.get(title='Play Quiz')

		learningpath = createlearningpath(section.id)

		comparelist = list()
		comparelist.append(lecture1)
		comparelist.append(quiz1)
		comparelist.append(quiz2)
		comparelist.append(lecture2)

		self.assertEqual(learningpath, comparelist)

	def test_news(self):
		test_activity = {
			"@context": "https://www.w3.org/ns/activitystreams",
			"summary": "test created new course test_course",
			"type": "create",
			"actor": "test",
			"object": "test_course",
			"published": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ%Z'),
		}
		test_list = list()
		lst = list()
		#lst.append(test_activity)
		#g = GetActivityStream()
		#test_list.append(g.checkValidity(g.convertToJson(lst)))

		a = ActivityStream_JSON()
		if a.check_validity(test_activity) == True:
			test_list.append(a.get_object())

		jsons_to_be_sent = list()
		new_list = list()
		isExist = False

		for v in reversed(test_list):
			isExist = False
			for n in new_list:
				if v.summary == n.summary:
					isExist = True
			if isExist == False:
				new_list.append(v)

		for i in range(20):
			if(len(new_list) > i):
				jsons_to_be_sent.append(new_list[i])

		def takeTime(elem):
			return datetime.strptime(elem.published,'%Y-%m-%dT%H:%M:%SZ')

		jsons_to_be_sent.sort(key = takeTime,reverse = True)

		self.assertEqual(jsons_to_be_sent[0].summary, test_activity["summary"])
