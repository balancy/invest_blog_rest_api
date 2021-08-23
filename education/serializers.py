from rest_framework import serializers

from .models import Course, Mentor, Student


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "id", "user", "fullname", "status", "bio"
        view_name = "mentors"


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "id", "user_id", "fullname", "status", "bio", "courses"

        view_name = "students"


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "id", "mentor", "title", "short_description", "full_description"
        view_name = "courses"
