from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):
    def setUp(self):
        """Creates about me content"""
        self.about = About(
            title="About title",                                      
            content="About content", 
            profile_image="placeholder",
            )
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
      


    def test_successful_collaborate_submission(self):
        """Test for posting a collaborate on about"""
           
        post_data = {
            'name':'abc',
            'email':'abc@e.com',
            'message' : 'This is a test massage.',
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )