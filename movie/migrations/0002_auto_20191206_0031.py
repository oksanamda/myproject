# Generated by Django 3.0 on 2019-12-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='begin_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='end_year',
            field=models.IntegerField(),
        ),
    ]