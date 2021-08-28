from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from education.models import Course, Mentor


class MentorViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        mixer.blend(Mentor)

    def test_mentors_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/mentors/')

        self.assertEqual(response.status_code, 200)

    def test_mentor_view_url_accessible_by_id(self):
        response = self.client.get('/api/mentors/1/')

        self.assertEqual(response.status_code, 200)


class StudentListViewTest(TestCase):
    def test_student_view_uses_correct_reverse_name(self):
        response = self.client.get(reverse('students-list'))
        another_response = self.client.get('/api/students/')

        self.assertEqual(response.content, another_response.content)

    def test_student_view_doesnt_use_any_templates(self):
        response = self.client.get(reverse('students-list'))

        self.assertIsNone(response.template_name)


class CourseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        mixer.blend(Course)

    def test_course_view_headers_match_standard_drf_headers(self):
        response = self.client.get('/api/courses/')

        self.assertEquals(response.headers['Content-Type'], 'application/json')
