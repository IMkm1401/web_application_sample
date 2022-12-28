from django.db import models
from django.contrib.auth.models import User
class Comments(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name+" "+self.family