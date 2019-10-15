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



