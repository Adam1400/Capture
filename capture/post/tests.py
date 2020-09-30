from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase

#from .author import add_author, delete_author, get_author, list_authors
#from .picture import add_picture, delete_picture, get_picture, list_pictures
#from .models import Author, Picture


class ViewTests(SimpleTestCase):

    def check_template(self, page, template):
        response = self.client.get(page)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, template_name=template)

    def test_view_index(self):
        self.check_template('/', 'base.html')

    def test_view_prototype(self):
        self.check_template('/index.html', 'index.html')
        self.check_template('/post.html', 'post.html')
        

    def test_view_no_page(self):
        response = self.client.get('/home.html')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, template_name='index.html')

    def test_view_missing_template(self):
        response = self.client.get('/xxx')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('index.html')

    def test_view_bad_url(self):
        response = self.client.get('/xxx/home.html')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('index.html')

