from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r"list/", RecommendationView.as_view(), name="recommendation-list"),
    url(r"(?P<pk>[0-9]+)/", Recommendation_deneme.as_view(), name="recommendation-deneme")
]
