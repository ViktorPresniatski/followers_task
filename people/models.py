from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    class Meta:
        db_table = 'people'

    def followings(self):
        array_of_followings = []
        for id in self.follow_ids.split():
            array_of_followings.extend(int(id))
        return array_of_followings

    def count_following(self):
        return len(self.follow_ids.split())

    def count_followers(self):
        count = 0
        for p in Person.objects.all():
            count += p.follow_ids.split().count(str(self.id))
        return count
