from django.test import SimpleTestCase
from django.urls import reverse,resolve
from foodsystem_app import views
from foodsystem_app.views import menu

class TestUrls(SimpleTestCase):
    
    def test_main_url_is_resolved(self):
        url = reverse('main')
        print(resolve(url))
        self.assertEquals(resolve(url).func, menu)
