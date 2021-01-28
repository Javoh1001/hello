from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def events(request):
    return render(request,'events.html')

def blog(request):
    return render(request, 'blog.html')

def teacher(request):
    return render(request,'teacher.html')

def teacher_single(request):
    return render(request, 'teacher-single.html')

def contact(request):
    return render(request,'contact.html')

def notice(request):
    return render(request, 'notice.html')

def notice_single(request):
    return render(request, 'notice-single.html')

def research(request):
    return render(request,'research.html')

def scholarship(request):
    return render(request, 'scholarship.html')

def course_single(request):
    return render(request, 'course-single.html')

def event_single(request):
    return render(request, 'event-single.html')

def blog_single(request):
    return render(request, 'blog-single.html')

    

