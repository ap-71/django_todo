from django.db import models
from django.contrib.auth.models import User


class ToDoAction(models.Model):
    title = models.TextField(null=False)
    description = models.TextField()
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
