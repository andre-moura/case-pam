from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField('Course', through='Enrollment')

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=10, blank=True, null=True)