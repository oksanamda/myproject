# Generated by Django 3.0 on 2019-12-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_remove_actor_namw'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='is_favorite',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]
