from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foodsystem_app.views.login_register import register_request, login_request
from foodsystem_app.views.menu import MenuView

class TestUrls(SimpleTestCase):
    def test_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_request)

    def test_login_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_request)

    def test_store_order_is_resolved(self):
        url = reverse('store_order')
        print(resolve(url))
        self.assertEquals(resolve(url).func, MenuView.store_order)
        