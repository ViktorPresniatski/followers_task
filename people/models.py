from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
    )

    class Meta:
        db_table = 'people'

    def follow(self, *people):
        self.following.add(*people)

    def unfollow(self, *people):
        self.following.remove(*people)

    # def followings(self):
    #     array_of_followings = []
    #     for id in self.follow_ids.split():
    #         array_of_followings.extend(int(id))
    #     return array_of_followings

    def count_following(self):
        return self.following.count()

    def count_followers(self):
        return self.followers.count()

    def __str__(self):
        return "id: {0}, name: {1}".format(self.id, self.name)
