from django.test import SimpleTestCase
from django.urls import reverse,resolve
from web_app.views import sugarfill,bpfill,billing,pharm

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse(('sugarfill'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,sugarfill)

    def test_list_url_is_resolved(self):
        url = reverse(('billing'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,billing)

    def test_list_url_is_resolved(self):
        url = reverse(('pharm'))
        print(resolve(url))
        self.assertEquals(resolve(url).func,pharm)

      
        
