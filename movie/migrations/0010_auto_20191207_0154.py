# Generated by Django 3.0 on 2019-12-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_actor_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='role',
            field=models.CharField(max_length=500),
        ),
    ]
