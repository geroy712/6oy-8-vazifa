from django.urls import path
from .views import home, course, lesson

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:course_id>/', course, name='course_by_type'),
    path('lesson/<int:lesson_id>/', lesson, name='lesson_detail'),
]