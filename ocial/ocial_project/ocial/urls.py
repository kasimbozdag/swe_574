from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from topics import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name= 'home'),
	path('accounts/', include('accounts.urls')),
    path('classroom/', include('topics.urls')),
    path('topics',views.topics, name= 'topics'),
    path('news',views.news, name= 'news'),
    path('<username>/', views.userprofile, name='userprofile'),
    path('<username>/followers', views.userfollowers, name='userfollowers'),
    path('<username>/following', views.userfollowing, name='userfollowing'),
    path('follow/<username>/', views.followuser, name='followuser'),
    path('unfollow/<username>/', views.unfollowuser, name='unfollowuser'),
    path('editprofile',views.editprofile, name= 'editprofile'),
    path('editprofile/changepassword',views.changepassword, name= 'changepassword'),
    path('explore',views.explore, name= 'explore'),
    path('exploretopic/<int:topic_id>',views.exploretopic, name= 'exploretopic'),
    path('exploreteacher/<id>',views.exploreteacher, name= 'exploreteacher'),
    path('course/<int:course_id>/', views.coursedetail, name = 'coursedetail'),
    path('enroll/<int:course_id>', views.enrollcourse , name='enrollcourse'),
    url('recommendation/', include('recommendation.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
