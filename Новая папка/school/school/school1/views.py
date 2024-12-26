from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Course, Lesson

def home(request: WSGIRequest):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'intex.html', context)

def course(request: WSGIRequest, course_id):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'course.html', context)
    
def lesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id= lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'lesson.html', context)
    




