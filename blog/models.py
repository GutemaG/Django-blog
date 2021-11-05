from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    DIFFICULTY_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('AD', 'Advance'),
    ]
    title = models.CharField(max_length=250)
    # body = models.TextField()
    # body = RichTextField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    difficulty = models.CharField(max_length=15,choices=DIFFICULTY_CHOICES,default="BEG",)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



