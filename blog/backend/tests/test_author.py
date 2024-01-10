from django.test import TestCase

from ..models import Author


class AuthorTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='TestName', email='email')
        Author.objects.create(name='TestName2', email='email2')

    def test_get_by_id(self):
        author = Author.get_by_id(1)
        self.assertEqual(author['name'], self.author.name)
        self.assertEqual(author['email'], self.author.email)

    def test_get_list(self):
        authors = Author.get_list()
        self.assertTrue(len(authors) == 2)
