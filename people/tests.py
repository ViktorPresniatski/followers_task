from django.test import TestCase

from .models import Person

class PersonTestCase(TestCase):

    def setUp(self):
        self.a = Person.objects.create(id = '1', name = 'a', )
        self.b = Person.objects.create(id = '2', name = 'b', )
        self.c = Person.objects.create(id = '3', name = 'c', )
        self.d = Person.objects.create(id = '4', name = 'd', )
        self.a.save()
        self.b.save()
        self.c.save()
        self.d.save()


    def test_count_following_with_two_followings(self):
        self.a.following.add(
            self.b,
            self.c,
        )
        self.assertEqual(self.a.count_following(), 2)

    def test_count_following_with_zero_followings(self):
        self.assertEqual(self.a.count_following(), 0)

    def test_count_followers_with_two_followers(self):
        self.b.following.add(self.c)
        self.a.following.add(self.c)
        self.assertEqual(self.c.count_followers(), 2)

    def test_count_followers_with_zero_followers(self):
        self.b.following.add(self.d)
        self.c.following.add(self.d)
        self.assertEqual(self.c.count_followers(), 0)
