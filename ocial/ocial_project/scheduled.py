import django

django.setup()
from django.contrib.auth.models import User
from recommendation.models import Recommendation
from recommendation.sparql_queries import query_common_p_o, query_most_common_p_s, common_instance_of
from topics.models import Learner_Course_Record, Course


def scheduled():
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
            ratingT = rating["c_p_o"] + rating["c_p_s"] + rating["c_i"]
            c = Course.objects.get(pk=course)
            recommendation = Recommendation(
                user=user,
                course_id=course,
                rating=ratingT,
                version=2,
            )
            print(user, course, ratingT, rating)
            recommendation.save()

    Recommendation.objects.filter(version=1).delete()
    print("all old recommendation are deleted")
    recommendations = Recommendation.objects.filter(version=2)
    for recommendation in recommendations:
        recommendation.version = 1
        recommendation.save()


scheduled()
