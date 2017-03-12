from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True,
    )

    class Meta:
        db_table = 'people'

    def follow(self, *people):
        people = filter(lambda p: p != self, people)
        self.following.add(*people)

    def unfollow(self, *people):
        self.following.remove(*people)

    def count_following(self):
        return self.following.count()

    def count_followers(self):
        return self.followers.count()

    def __str__(self):
        return "id: {0}, name: {1}".format(self.id, self.name)
