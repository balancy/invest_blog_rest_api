from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Course, Mentor, Student
from .serializers import CourseSerializer, MentorSerializer, StudentSerializer


class MentorsViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['mentor', 'title']
    ordering_fields = ['title', 'id']
