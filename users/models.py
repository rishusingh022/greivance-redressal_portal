from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    category = models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    body=models.TextField()

    def __str__(self):
        return self.category + '|' + str(self.title)
