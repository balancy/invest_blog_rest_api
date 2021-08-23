from django.contrib import admin

from education.models import Course, Mentor, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "mentor"
    raw_id_fields = "mentor",


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = "id", "fullname", "user", "status"
    raw_id_fields = "user",


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "fullname", "user", "status"
    raw_id_fields = "user",
