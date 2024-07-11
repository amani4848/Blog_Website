from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date_published = models.DateField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_posted = models.DateField(null=True)

    def __str__(self):
        return self.content


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name