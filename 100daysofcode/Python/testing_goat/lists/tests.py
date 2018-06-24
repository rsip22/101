from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
