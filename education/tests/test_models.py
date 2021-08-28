from django.test import TestCase
from education.models import Course, Mentor, Student
from mixer.backend.django import mixer


class MentorModelTest(TestCase):
    def test_fullname_label(self):
        field_label = Mentor._meta.get_field("fullname").verbose_name
        self.assertEqual(field_label, "Полное имя")

    def test_fullname_max_length(self):
        max_length = Mentor._meta.get_field('fullname').max_length
        self.assertEqual(max_length, 200)


class StudentModelTest(TestCase):
    def test_default_status_blank_attribute(self):
        status_is_blank = Student._meta.get_field("status").blank
        self.assertTrue(status_is_blank)

    def test_object_name_is_in_correct_format(self):
        student = mixer.blend(Student)
        expected_object_name = f'Student <{student.fullname}>'
        self.assertEqual(str(student), expected_object_name)


class CourseModelTest(TestCase):
    def test_unnecessary_fields_by_default_are_empty(self):
        course = mixer.blend(Course)
        self.assertTrue(not course.title)
        self.assertTrue(not course.short_description)
        self.assertTrue(not course.full_description)
