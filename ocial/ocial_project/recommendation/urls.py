from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r"list/",Recommendation.as_view(),name="recommendation-list")
]