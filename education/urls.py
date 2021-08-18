from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('mentors', views.MentorsViewSet)
router.register('courses', views.CoursesViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
