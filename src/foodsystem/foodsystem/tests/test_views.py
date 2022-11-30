from django.test import TestCase, Client
from django.urls import reverse
from foodsystem_app.models import discount,menu
import json

class TestViews(TestCase):
    
    def test_login_GET(self):
        client = Client()

        response = client.get(reverse('login'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_main_menu_GET(self):
        client = Client()

        response = client.get(reverse('menu'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'mainmenu.html')

    def test_register_GET(self):
        client = Client()

        response = client.get(reverse('register'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
