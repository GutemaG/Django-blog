from django.db import models
from django.contrib.auth.models import User

from PIL import Image # pillow for  resizing the profile image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile')

    def __str__(self):
        return self.user.username
'''
    def save(self):
        super().save()

        image =Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.image.path)
'''