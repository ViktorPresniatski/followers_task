# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170311_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='people.Person'),
        ),
    ]
