from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.classroom, name= 'classroom'),
    path('coursestatistics/<int:course_id>/',views.coursestatistics, name= 'coursestatistics'),
    path('sectionstatistics/<int:section_id>/',views.sectionstatistics, name= 'sectionstatistics'),
    path('profile',views.profile, name= 'profile'),
    path('profile/changepassword',views.changepassword, name= 'changepassword'),
    path('teacher',views.teacher, name= 'teacher'),
	path('newcourse',views.newcourse, name= 'newcourse'),
	path('editcourse/<int:course_id>/', views.editcourse, name = 'editcourse'),
	path('editcourse/<int:course_id>/glossary/', views.glossary, name = 'glossary'),
	path('editsection/<int:section_id>/', views.editsection, name = 'editsection'),
	path('editlecture/<int:lecture_id>/', views.editlecture, name = 'editlecture'),
	path('editquiz/<int:quiz_id>/', views.editquiz, name = 'editquiz'),
    path('editquestion/<int:question_id>/', views.editquestion, name = 'editquestion'),
	path('deletecourse/<int:course_id>/', views.deletecourse, name = 'deletecourse'),
    path('deletelabel/<int:course_id>/<int:label_id>/', views.deletelabel, name = 'deletelabel'),
    path('deletesection/<int:section_id>/', views.deletesection, name = 'deletesection'),
    path('deleteresource/<int:resource_id>/', views.deleteresource, name = 'deleteresource'),
    path('deletelecture/<int:lecture_id>/', views.deletelecture, name = 'deletelecture'),
    path('deletequiz/<int:quiz_id>/', views.deletequiz, name = 'deletequiz'),
    path('deletequestion/<int:question_id>/', views.deletequestion, name = 'deletequestion'),
    path('deletechoice/<int:choice_id>/', views.deletechoice, name = 'deletechoice'),
    path('deleteglossary/<int:glossary_id>/', views.deleteglossary, name = 'deleteglossary'),
    path('newglossary/<int:course_id>/<str:wiki_id>', views.newglossary, name = 'newglossary'),
    path('learner',views.learner, name= 'learner'),
    path('viewcourse/<int:course_id>', views.viewcourse, name = 'viewcourse'),
    path('viewcourse/<int:course_id>/glossary/', views.viewglossary, name = 'viewglossary'),
    path('viewsection/<int:section_id>/', views.viewsection, name = 'viewsection'),
    path('viewlecture/<int:lecture_id>/', views.viewlecture, name = 'viewlecture'),
    path('viewquiz/<int:quiz_id>/', views.viewquiz, name = 'viewquiz'),
    path('unenroll/<int:course_id>/', views.unenrollcourse, name = 'unenrollcourse'),


]
