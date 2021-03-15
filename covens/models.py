from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

class Coven(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    leader = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name