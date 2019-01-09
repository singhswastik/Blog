from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_services_page_status_code(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

    def test_category_page_status_code(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page_status_code(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
