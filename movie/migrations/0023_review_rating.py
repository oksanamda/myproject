# Generated by Django 2.2.8 on 2019-12-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0022_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=3),
        ),
    ]