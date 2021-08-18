from rest_framework import serializers

from .models import Course, Mentor


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "id", "user", "status", "bio"
        view_name = "mentors"


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "id", "mentor", "title", "description"
        view_name = "courses"
