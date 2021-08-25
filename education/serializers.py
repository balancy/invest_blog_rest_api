from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Course, Mentor, Student


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "id", "fullname", "status", "bio"
        view_name = "mentors"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "id", "user_id", "fullname", "status", "bio", "courses"
        view_name = "students"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "id", "mentor", "students", "title", "short_description", "full_description"
        view_name = "courses"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 2
        fields = "username", "is_superuser", "student", "mentor"
        view_name = "users"
