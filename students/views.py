from django.shortcuts import render
from rest_framework.response import Response
from .serializer import StudentSerializer,ClassSerializer,TeacherSerializer
from rest_framework import generics
from .models import Student,Class,Teacher
# Create your views here.


class StudentCreateListView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # queryset = Student.objects.prefetch_related('teacher').all()


class StudentDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class ClassCreateListView(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class ClassDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class TeacherCreateListView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherDetailedView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

