from django.db import models
from model_utils.models import TimeStampedModel
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, unique=True)
    teacher_code = models.CharField(max_length=100,)
    teacher_age = models.IntegerField(max_length=10, unique=True)

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=100, unique=True)
    student_code = models.CharField(max_length=100)
    student_age = models.IntegerField(max_length=100, unique=True)

    def __str__(self):
        return self.student_name
    
class ClassRoom(TimeStampedModel):
    room_name = models.CharField(max_length=100, unique=True)
    teacher_course = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.room_name
    