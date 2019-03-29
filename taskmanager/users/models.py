from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    created_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    