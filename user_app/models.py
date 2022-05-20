from django.db import models
from django.urls import reverse
# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,blank=False)

    def get_absolute_url(self):
        return reverse("user_app:new", kwargs={})
    

    def __str__(self):
        return self.name
