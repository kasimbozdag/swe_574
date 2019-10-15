from django.contrib import admin
from .models import *


admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Learner_Course_Record)
admin.site.register(Learner_Section_Record)
admin.site.register(Learner_Lecture_Record)
admin.site.register(Learner_Quiz_Record)
admin.site.register(Label)
admin.site.register(Glossary)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Resource)