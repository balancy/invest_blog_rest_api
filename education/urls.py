from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('mentors', views.MentorsViewSet)
router.register('courses', views.CoursesViewSet)
router.register('students', views.StudentsViewSet)
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
