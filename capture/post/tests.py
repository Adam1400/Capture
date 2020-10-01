from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from .models import Post
from . import views
from django.db import models
from django.contrib.auth.models import User

# test views
class ViewTests(TestCase):  
    def check_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')

    def check_base_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='base.html')

    def check_styles_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='styles.html')

    def check_post(self):
        response = self.client.get('/post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='post.html') 

    def check_base_post(self):
        response = self.client.get('/post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='base.html') 

    def check_styles_posts(self):
        response = self.client.get('/post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='styles.html')

    def check_admin(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

    def check_null(self):
        responce =  self.client.get('/xxxxx')
        seldf.assertEqual(responce.status_code, 404)


# test content
class ContentTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
        user= 'adam1400',
        comment= 'Testing database...',
        content= 'https://arts.unco.edu/images/music/campus-commons/CCPH_Interior_1200x800.jpg',
        post_date= 'September 28, 2020'    
        )

    def test_post_content(self):
        self.assertEqual(post.user , 'adam1400')
        self.assertEqual(post.comment, 'Testing database...')
        self.assertEqual(post.content, 'https://arts.unco.edu/images/music/campus-commons/CCPH_Interior_1200x800.jpg')
        self.assertEqual(post.post_date, 'September 28, 2020')


        


    

