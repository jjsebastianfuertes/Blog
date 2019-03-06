from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # add date only when te post is added, not during updates
    date_posted = models.DateTimeField(auto_now_add=True)
    # if an user is deleted all his post are deled, not viceversa
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
