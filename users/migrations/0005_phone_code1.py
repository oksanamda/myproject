# Generated by Django 2.2.8 on 2019-12-19 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20191219_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='code1',
            field=models.OneToOneField(default='000000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
