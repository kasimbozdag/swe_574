from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from accounts.models import *
import requests
import json



class Topic(models.Model):
	title = models.CharField(max_length=200,unique=True)

	def __str__(self):
		return self.title

class Course(models.Model):
	title = models.CharField(max_length=200,blank=False)
	pubdate = models. DateTimeField()
	image = models.ImageField(upload_to='images/', default= '../static/default.jpg')
	description = models.TextField(blank=True)
	wywl = models.TextField(blank=True)
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)
	topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
	published = models.BooleanField(default=False)
	course_learner = models.ManyToManyField(Learner, blank=True,through='Learner_Course_Record')
	isPublishable = models.BooleanField(default=False)
	completeRate = models.DecimalField(default= 0,max_digits=5,decimal_places=1)
	numberofLearners = models.IntegerField(default= 0)



	def pub_date_exact(self):
		return self.pubdate.strftime('%e %B %Y %H:%M')


	def pub_date(self):
		return self.pubdate.strftime('%e %B %Y')

	def __str__(self):
		return self.title

	def summary(self):
		return self.description[:200]

class Learner_Course_Record(models.Model):
	learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	isFinished = models.BooleanField(default=False)
	completeRate = models.DecimalField(default= 0, max_digits=5,decimal_places=1)

	def __str__(self):
		return self.learner.user.username + " - " +self.course.title

class Glossary(models.Model):
	identifier=models.CharField(max_length=32,default="")
	name = models.CharField(max_length=200)
	image_url = models.CharField(max_length=1000, blank=True)
	description = models.TextField(blank=True)
	url = models.CharField(max_length=1000, blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)


	def __str__(self):
		return self.name

class Section(models.Model):
	name = models.CharField(max_length=200)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
	order =  models.IntegerField(default=1)
	description = models.TextField(blank=True)
	section_learner = models.ManyToManyField(Learner, blank=True,through='Learner_Section_Record')
	isLinked = models.BooleanField(default=False)
	isPublishable = models.BooleanField(default=False)
	completeRate = models.DecimalField(default= 0, max_digits=5,decimal_places=1)



	class Meta:
		ordering = ['order']

	def __str__(self):
		return self.name

class Learner_Section_Record(models.Model):
	learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	isFinished = models.BooleanField(default=False)
	completeRate = models.DecimalField(default= 0, max_digits=5,decimal_places=1)

	def __str__(self):
		return self.learner.user.username + " - " +self.section.name

class Lecture(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(blank=True)
	section = models.ForeignKey('Section', on_delete=models.CASCADE)
	order =  models.IntegerField(default=1)
	lecture_learner = models.ManyToManyField(Learner, blank=True,through='Learner_Lecture_Record')
	completeRate = models.DecimalField(default= 0, max_digits=5,decimal_places=1)



	class Meta:
		ordering = ['order']
		verbose_name = 'Lecture'

	def __str__(self):
		return self.title

class Learner_Lecture_Record(models.Model):
	learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
	lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
	isFinished = models.BooleanField(default=False)

	def __str__(self):
		return self.learner.user.username + " - " +self.lecture.title

class Quiz(models.Model):
	title = models.CharField(max_length=200)
	section = models.ForeignKey('Section', on_delete=models.CASCADE)
	order =  models.IntegerField(default=1)
	successrate =  models.IntegerField(default=0)
	quiz_learner = models.ManyToManyField(Learner, blank=True,through='Learner_Quiz_Record')
	isPublishable = models.BooleanField(default=False)
	completeRate = models.DecimalField(default= 0, max_digits=5,decimal_places=1)



	class Meta:
		ordering = ['order']
		verbose_name = 'Quiz'

	def __str__(self):
		return self.title

class Learner_Quiz_Record(models.Model):
	learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	isFinished = models.BooleanField(default=False)

	def __str__(self):
		return self.learner.user.username + " - " +self.quiz.title

class Question(models.Model):
	title = models.TextField(blank=True)
	quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
	order =  models.IntegerField(default=1)
	isPublishable = models.BooleanField(default=False)


	class Meta:
		ordering = ['order']
		verbose_name = 'Question'

	def __str__(self):
		return self.title

class Choice(models.Model):
	title = models.TextField(blank=True)
	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	order =  models.IntegerField(default=1)
	isTrue = models.BooleanField(default=False)


	class Meta:
		ordering = ['order']
		verbose_name = 'Choice'

	def __str__(self):
		return self.title

class Resource(models.Model):
	name = models.CharField(max_length=200, blank=True)
	link = models.FileField(upload_to='sources/', blank=True)
	section = models.ForeignKey('Section', on_delete=models.CASCADE)


	def __str__(self):
		return self.name

class ActivityStream_JSON(models.Model):
	context = models.CharField(max_length=200, blank=True)
	summary = models.CharField(max_length=200, blank=True)
	type = models.CharField(max_length=200, blank=True)
	actor = models.CharField(max_length=200, blank=True)
	object = models.CharField(max_length=200, blank=True)
	published = models.CharField(max_length=200, blank=True)
	imgUrl = models.CharField(max_length=200, blank=True)
	keysArray = ['@context', 'summary', 'type', 'actor', 'object', 'published']



	def check_validity(self,json_data):

		for key in self.keysArray:
			if not key in json_data:
				return False

		self.summary = json_data['summary']
		self.type = json_data['type']
		self.actor = json_data['actor']
		self.object =  json_data['object']
		self.published =  json_data['published']

		return True

	def get_object(self):
		return self

activityHost = "http://activity_stream:3000/"
class GetActivityStream(models.Model):

	def getFollowedActivities(self,request):
		userprofile = UserProfile.objects.get(user=request.user)
		following_q = userprofile.user.following.all()
		responses = list()
		json_datas = list()
		print("current")
		for usr in following_q:
			r = requests.get(activityHost + "getAllActivities?actor=" + request._current_scheme_host + "/" + usr.following.username+"/")
			responses.append(r)

		json_datas = self.convertToJson(responses)

		return self.checkValidity(json_datas)


	def getMyActivities(self,request):
		responses = list()
		json_datas = list()
		r = requests.get(activityHost + "getAllActivities?actor=" + request._current_scheme_host + "/" + request.user.username+"/")
		responses.append(r)
		json_datas = self.convertToJson(responses)
		return self.checkValidity(json_datas)

	def getActivitiesProfile(self,request,username):
		responses = list()
		json_datas = list()
		r = requests.get(activityHost + "getAllActivities?actor=" + request._current_scheme_host + "/" + username + "/")
		responses.append(r)
		json_datas = self.convertToJson(responses)
		return self.checkValidity(json_datas)

	def getPeopleThatFollowMe(self,request):
		responses = list()
		json_datas = list()
		r = requests.get(activityHost + "getAllActivities?object=" + request._current_scheme_host + "/" + request.user.username)
		responses.append(r)
		json_datas = self.convertToJson(responses)
		return self.checkValidity(json_datas)


	def checkValidity(self,data_list):
		valid_jsons = list()
		for json_data_ in data_list:
			data = json.loads(json_data_)
			test = ActivityStream_JSON()
			isValid = test.check_validity(data)
			if isValid:
				valid_jsons.append(test.get_object())
		return valid_jsons

	def convertToJson(self,data_list):
		print("following : ")
		json_datas = list()
		for res in data_list:
			res = res.json()

			if res is not None:
				for r in res:
					json_datas.append(json.dumps(res.get(r)))
					#print("aaaa" + json.dumps(res.get(r)))
		return json_datas
