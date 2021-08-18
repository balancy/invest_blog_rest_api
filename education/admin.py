from django.contrib import admin

from education.models import Course, Mentor


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "mentor"
    raw_id_fields = "mentor",


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = "id", "user", "status"
    raw_id_fields = "user",
