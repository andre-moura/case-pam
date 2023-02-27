from django.shortcuts import render, get_object_or_404
from .models import Course, Student, Enrollment

def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'students': students, 'courses': courses})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    enrollments = Enrollment.objects.filter(student=student_id)
    return render(request, 'student_detail.html', {'student': student, 'enrollments': enrollments})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollments = Enrollment.objects.filter(course=course_id)
    return render(request, 'course_detail.html', {'course': course, 'enrollments': enrollments})