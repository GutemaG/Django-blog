# Generated by Django 3.2.9 on 2021-11-05 16:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
