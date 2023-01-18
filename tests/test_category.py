from django.test import TestCase
from utils.base_url import get_url
from category.models import Category
from unittest.mock import patch


class TestCategory(TestCase):
    def test_problem_category_is_created(self):
        self.category = Category.objects.create(name_cat="jose")

        self.assertIsInstance(
            self.category,
            Category
        )

    def test_view_uri_django(self):
        api_url = get_url()
        response = self.client.get(f'{api_url}/category/django', verify=False)

        with patch('requests.get') as fake_quest:
            fake_quest.return_value.ok = False

            self.assertEqual(
                200,
                response.status_code
            )

    def test_view_uri_python(self):
        api_url = get_url()
        response = self.client.get(f'{api_url}/category/python', verify=False)

        self.assertEqual(
            200,
            response.status_code
        )

    def test_view_uri_tecnologia(self):
        api_url = get_url()
        response = self.client.get(f'{api_url}/category/tecnologia', verify=False)

        self.assertEqual(
            200,
            response.status_code
        )

    def test_view_uri_sistema(self):
        api_url = get_url()
        response = self.client.get(f'{api_url}/category/sistema', verify=False)

        self.assertEqual(
            200,
            response.status_code
        )