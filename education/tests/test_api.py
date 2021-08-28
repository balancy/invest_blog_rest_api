import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from mixer.backend.django import mixer

from education.models import Course, Mentor


class MentorApiTest(TestCase):
    def test_mentor_api_create_5_instances(self):
        instances_number = 5
        mixer.cycle(instances_number).blend(Mentor)

        self.assertEqual(Mentor.objects.count(), instances_number)

    def test_mentor_api_response_content(self):
        mixer.cycle(2).blend(Mentor)
        response = self.client.get('/api/mentors/2/')

        self.assertEqual(
            json.loads(response.content),
            {
                'id': 2,
                'bio': '',
                'status': '',
                'fullname': '',
            }
        )

class StudentApiTest(TestCase):

    def test_mentor_api_post_response_for_default_user(self):
        user = mixer.blend(get_user_model())
        response = self.client.post('/api/students/', {'user': user})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.content,
            b'{"detail":"Authentication credentials were not provided."}',
        )