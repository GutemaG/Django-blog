# Generated by Django 3.2.9 on 2021-11-24 10:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookmarked',
            new_name='Bookmarked2',
        ),
    ]
