from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views import View

from recommendation.models import Recommendation
from recommendation.sparql_queries import query_common_p_o, query_most_common_p_s, common_instance_of
from topics.models import Course, Learner_Course_Record, UserProfile


class RecommendationView(View):
    def get(self, request):
        recommendations = Recommendation.objects.filter(user=request.user, version=1).order_by("-rating")[:10]
        rec_courses = [recommendation.course for recommendation in recommendations]
        if not rec_courses:
            courses = Learner_Course_Record.objects.filter(learner__user=request.user).order_by("-pubdate")

            taken_courses = [course.course.id for course in courses]

            rec_courses = Course.objects.filter(published=True).exclude(id__in=taken_courses).exclude(teacher=request.user)

        return render(request, 'recommendation/recommendation.html', {"courses": rec_courses})


"""
class Recommendation(View):
    def get(self, request):
        courses = Learner_Course_Record.objects.filter(learner__user=request.user)

        taken_courses = [course.course.id for course in courses]

        labels = [label.identifier for course in courses for label in course.course.glossary_set.all()]

        from collections import Counter

        labels_count = Counter(labels)

        rec = {}
        for label in labels_count:
            c = Course.objects.filter(glossary__identifier=label).exclude(id__in=taken_courses).exclude(teacher=request.user)
            for course in c:
                if course.id in rec:
                    rec[course.id] += labels_count[label]
                else:
                    rec[course.id] = labels_count[label]
        sorted_rec = sorted(rec.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        rec_courses = []
        for s in sorted_rec:
            rec_courses.append(Course.objects.get(id=s[0]))
            if len(rec_courses) > 4:
                break

        return render(request, 'recommendation/recommendation.html', {"courses": rec_courses})
"""


class Recommendation_deneme(View):
    def get(self, request):

        users = User.objects.all()
        for user in users:
            courses = Learner_Course_Record.objects.filter(learner__user=user)

            taken_courses = [course.course.id for course in courses]

            labels = [label.identifier for course in courses for label in course.course.glossary_set.all()]
            course_labels = {}
            courses = Course.objects.filter(published=True).exclude(id__in=taken_courses).exclude(teacher=user)
            for course in courses:
                c_labels = [label.identifier for label in course.glossary_set.all()]
                course_labels[course.id] = c_labels
            rating = {}
            for course in course_labels:
                r = query_common_p_o(labels, course_labels[course])
                rating["c_p_o"] = 0
                if r:
                    rating["c_p_o"] = r['ocount_ratio'] + r['pcount_ratio'] + r['scount_ratio']
                q = query_most_common_p_s(labels, course_labels[course])

                rating["c_p_s"] = 0
                if q:
                    rating["c_p_s"] = q['ocount_ratio'] + q['pcount_ratio'] + q['scount_ratio']

                s = common_instance_of(labels, course_labels[course])

                rating["c_i"] = 0
                if s:
                    rating["c_i"] = s['ratio']
                print(user, course, rating)
        return render(request, 'recommendation/recommendation.html', {"courses": {}})
