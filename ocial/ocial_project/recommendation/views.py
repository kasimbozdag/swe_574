from django.shortcuts import render

# Create your views here.
from django.views import View

from topics.models import Course, Learner_Course_Record


class Recommendation(View):
    def get(self,request):
        courses = Learner_Course_Record.objects.filter(learner__user=request.user)

        taken_courses = [course.course.id for course in courses]
        print(taken_courses)
        labels = [label.id for course in courses for label in course.course.label.all()]
        from collections import Counter

        labels_count = Counter(labels)
        rec = {}
        for label in labels_count:
            c = Course.objects.filter(label__id=label).exclude(id__in=taken_courses).exclude(teacher=request.user)
            for course in c:
                if course.id in rec:
                    rec[course.id] += labels_count[label]
                else:
                    rec[course.id] = labels_count[label]
        sorted_rec=sorted(rec.items(), key=lambda kv:(kv[1], kv[0]),reverse=True)
        rec_courses=[]
        for s in sorted_rec:
            rec_courses.append(Course.objects.get(id=s[0]))
            if len(rec_courses)>4:
                break

        return render(request, 'recommendation/recommendation.html', {"courses": rec_courses})
