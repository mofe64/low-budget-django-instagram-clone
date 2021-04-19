from django.db import models


# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(null=True)
    profile_Picture = models.ImageField(default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
