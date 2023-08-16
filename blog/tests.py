from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your tests here.


class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(username='ali')
        cls.post1 = Post.objects.create(title='test1',
                                        text='salam',
                                        author=cls.user1,
                                        status=Post.STATUS_CHOICES[0][0])
        cls.post2 = Post.objects.create(title='test2',
                                        text='khodafez',
                                        author=cls.user1,
                                        status=Post.STATUS_CHOICES[1][0])

    def test_list_page_by_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_list_page_by_name(self):
        response = self.client.get(reverse('post_page'))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_by_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_page_by_name(self):
        response = self.client.get(reverse('detail_page', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post1_exist_in_list_page(self):
        response = self.client.get('/blog/')
        self.assertContains(response, 'test1')

    def test_post1_exist_in_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)

    def test_post_not_exist_in_db(self):
        response = self.client.get('/blog/1000/')
        self.assertEqual(response.status_code, 404)

    def test_post_pub_or_drf(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'test1')
        self.assertEqual(self.post2.text, 'khodafez')

    def test_create_view(self):
        response = self.client.post(reverse('new_page'), {
            'title': 'test3',
            'text': 'this is',
            'status': 'pub',
            'author': self.user1.id

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'test3')
        self.assertEqual(Post.objects.last().text, 'this is')

    def test_update_view(self):
        response = self.client.post(reverse("update_page", args=[self.post1.id]), {
            'title': 'salamo',
            'text': 't'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'salamo')
        self.assertEqual(Post.objects.last().text, 't')


    def test_delete_view(self):
        response = self.client.post(reverse("delete_page", args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)




