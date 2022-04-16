from audioop import reverse
from urllib import response
from django.test import SimpleTestCase

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code,200)
    def test_template_name_correct(self):  # new
        response = self.client.get("/home")
        self.assertTemplateUsed(response, "home.html")
    def test_template_content(self):  # new
        response = self.client.get("/home")
        self.assertContains(response, "<h1>Hello my name is Nikolay</h1>")   
    
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code,200)
    def test_template_name_correct(self):  # new
        response = self.client.get("/about")
        self.assertTemplateUsed(response, "about.html")
    def test_template_content(self):
        response = self.client.get("/about")
        self.assertContains(response, "<h1>I am a student</h1>")        