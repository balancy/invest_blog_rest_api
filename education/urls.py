from django.db.models import base
from django.urls import path, include
from django.urls.base import reverse
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('mentors', views.MentorsViewSet, basename='mentors')
router.register('courses', views.CoursesViewSet, basename='courses')
router.register('students', views.StudentsViewSet, basename='students')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
