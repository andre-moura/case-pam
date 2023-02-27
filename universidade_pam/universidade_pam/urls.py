from django.urls import path
from . import views

app_name = 'universidade_pam'

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]