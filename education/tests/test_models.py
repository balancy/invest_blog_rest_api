from django.contrib.auth import get_user_model
from django.test import TestCase

from education.models import Course, Mentor, Student


class MentorModelTest(TestCase):
    def test_fullname_label(self):
        field_label = Mentor._meta.get_field("fullname").verbose_name
        self.assertEqual(field_label, "Полное имя")

    def test_fullname_max_length(self):
        max_length = Mentor._meta.get_field('fullname').max_length
        self.assertEqual(max_length, 200)


class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create(
            first_name='user2',
            email='user2@gmail.com',
            username='user2',
            password='pass',
        )

        Student.objects.create(
            user=user,
            fullname="Mike Tyson",
        )

    def test_default_status_blank_attribute(self):
        status_is_blank = Student._meta.get_field("status").blank
        self.assertTrue(status_is_blank)

    def test_object_name_is_in_correct_format(self):
        student = Student.objects.first()
        expected_object_name = f'Student <{student.fullname}>'
        self.assertEqual(str(student), expected_object_name)


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create(
            first_name='user3',
            email='user3@gmail.com',
            username='user3',
            password='pass',
        )

        mentor = Mentor.objects.create(
            user=user,
            fullname="Peter Parker",
        )

        Course.objects.create(
            mentor=mentor,
            title="new course",

        )

    def test_default_short_description_is_empty(self):
        course = Course.objects.first()
        self.assertTrue(not course.short_description)
