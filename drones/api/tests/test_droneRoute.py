""" Post tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from drones.api.models import Drone



class PostAPITestCase(APITestCase):
    """ Posts API test case. """

    def setUp(self):
        self.url = '/api/drone/'
        self.data = [
            {
            'serial_number': 'asdlasdl111111',
            'model': 'MI',
            'weight_limit': 200,
            'battery_capacity': 80
            },
            {
                'serial_number': 'OtherCode1',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },

            {
                'serial_number': 'OtherCode3',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode4',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode5',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode6',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode7',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode8',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode9',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode10',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            },
            {
                'serial_number': 'OtherCode11',
                'model': 'LI',
                'weight_limit': 200.50,
                'battery_capacity': 100
            }
        ]

        self.data1 = {
            'serial_number': 'asdlasdl111111',
            'model': 'MI',
            'weight_limit': 200,
            'battery_capacity': 80
        }

        
        self.data_error = {
            'serial_number': 'Im a great body'
        }

    def test_list_post_response_success(self):
        """ List of post with successful response. """
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_detail_post_response_success(self):
        """ Detail of a post with successful response. """
        for x in range(len (self.data) -1):
            post = Drone.objects.create(**self.data[x])
            request = self.client.get(self.url + str(post.id) + "/")
            self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_new_post_response_success(self):
        """ Create new post with successful response. """
        request = self.client.post(self.url, self.data1)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_load_drone_with_med(self):
        """ Load a drone with a med """


    def test_create_new_post_response_error(self):
        """ Create new post without title field, and with error response. """
        request = self.client.post(self.url, self.data_error)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_post_response_success(self):
        """ Create new post with successful response. """
        request = self.client.post(self.url, self.data1)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    