from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    teacher = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)  
    teacher = models.CharField(max_length=255, null=True)
    content = models.TextField()  
    duration = models.DurationField(blank=True, null=True)  
    created_at = models.DateField(blank=True, null=True)  
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)  

    def __str__(self):
        return self.title
