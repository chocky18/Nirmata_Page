from django.test import TestCase

from ..models import Post, Author


class PostTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='TestName', email='email')
        self.post = Post.objects.create(title='Test slug', text='asd qwe', author=self.author)
        Post.objects.create(title='Test slug 2', text='asd qwe 123', author=self.author)

    def test_get_by_slug(self):
        post = Post.get_by_slug('test-slug')
        self.assertEqual(post['slug'], self.post.slug)
        self.assertEqual(post['title'], self.post.title)

    def test_get_list(self):
        posts = Post.get_list()
        self.assertTrue(len(posts) == 2)
