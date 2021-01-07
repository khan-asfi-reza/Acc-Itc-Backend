from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
import mock
from django.core.files import File

file_mock = mock.MagicMock(spec=File, name='FileMock')


# Create your tests here.

class MainTestCase(TestCase):

    def get_client(self):
        self.client = APIClient()
        return self.client

    # Test OK -> Done
    def test_response_message_factory(self):
        factory = self.get_client()
        url = reverse('message-response')
        response = factory.post(url, {'name': 'Name', 'email': 'email@email.com', 'message': "Test Message"},
                                format='json')
        self.assertEqual(response.status_code, 201)
        response_2 = factory.post(url, {'name': 'Name', 'message': "Test Message"},
                                  format='json')
        self.assertEqual(response_2.status_code, 400)

    # Test Done -> Ok
    def test_panel_members(self):
        panel_post = PanelPost.objects.create(post_name="Admin")
        self.assertEqual(panel_post.post_name, "Admin")
        test_name = ["Test_User_1", "Test_User_2"]
        for each_test_name in test_name:
            members = PanelMember(name=each_test_name,
                                  year_start=2021,
                                  year_end=2022,
                                  picture=file_mock,
                                  social_link="http://127.0.0.1:8000",
                                  email=f"{test_name}e@m.com",
                                  post=panel_post,
                                  phone_number="1234566",
                                  post_type=1
                                  )

        factory = self.get_client()
        url = reverse('panel-members')
        response = factory.get(url)
        self.assertEqual(response.status_code, 200)
