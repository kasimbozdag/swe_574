from django.core.exceptions import PermissionDenied
from .models import *

def course_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['course_id'])
        if course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def glossary_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        glossary = Glossary.objects.get(pk=kwargs['glossary_id'])
        if glossary.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def section_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        section = Section.objects.get(pk=kwargs['section_id'])
        if section.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def lecture_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        lecture = Lecture.objects.get(pk=kwargs['lecture_id'])
        if lecture.section.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def quiz_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=kwargs['quiz_id'])
        if quiz.section.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def question_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs['question_id'])
        if question.quiz.section.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def choice_teacher_is_user(function):
    def wrap(request, *args, **kwargs):
        choice = Choice.objects.get(pk=kwargs['choice_id'])
        if choice.quiz.section.course.teacher == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap