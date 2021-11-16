from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

def validate_positive(value):
    if value <=0:
         raise ValidationError(
            _('invalid number'),
            params={'value': value},
        )

'''
def default_cover_image(self):
    if self.categories.name =="Technology":
        return 'default/technology.jpg'
    elif self.categories.name =="Programming":
        return 'default/programming.jpg'
    else:
        return 'default/default.jpg'
'''

class Blog(models.Model):
    DIFFICULTY_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('AD', 'Advance'),
    ]
    cover_image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=250)
    description = models.TextField()

    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    difficulty = models.CharField(
        max_length=15, choices=DIFFICULTY_CHOICES, default="BEG")
    tags = models.ManyToManyField(Tag, blank=False)
    categories = models.ManyToManyField(Category, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-updated_at']

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return "True" if self.liked else "False"
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


'''
/**
  TODO Add Bookmark for blogs
*/
'''