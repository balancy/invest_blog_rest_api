from blog.permissions import IsAdminUserOrReadOnly
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Course, Mentor, Student
from .serializers import (CourseSerializer, MentorSerializer,
                          StudentSerializer, UserSerializer)


class MentorsViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ('update',):
            self.permission_classes = [IsAuthenticated,]
        else:
            self.permission_classes = [IsAdminUserOrReadOnly]
        return super(self.__class__, self).get_permissions()


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['mentor', 'students', 'title']
    ordering_fields = ['title', 'id']


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def retrieve(self, request, pk=None):
        queryset = get_user_model().objects.filter(username=pk)
        user = queryset.first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
