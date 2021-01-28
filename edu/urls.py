from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('blog/', views.blog, name='blog'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher-single/', views.teacher_single, name = 'teacher-single'),
    path('contact/', views.contact, name='contact'),
    path('notice/', views.notice, name='notice'),
    path('notice-single/', views.notice_single, name ='notice-single'),
    path('research/', views.research, name='research'),
    path('scholarship/', views.scholarship, name='scholarship'),
    path('course-single/', views.course_single, name='course-single'),
    path('event-single/', views.event_single, name='event-single'),
    path('blog-single/', views.blog_single, name='blog-single')
]