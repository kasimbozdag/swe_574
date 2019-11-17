from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ocial.urls import *
from topics.views import news

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('news')
        print(resolve(url))
        self.assertEquals(resolve(url).func, news)
