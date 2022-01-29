from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer


class StudentCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Student
    queryset = Student.objects.all(),
    serializer_class = StudentSerializer


class StudentList(generics.ListAPIView):
    # API endpoint that allows Student to be viewed.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Student record to be updated.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a student record to be deleted.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer