from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    group = models.IntegerField()


class Article(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    image = models.CharField(max_length=100)


class BasicData(models.Model):
    name = models.TextField()
    source = models.TextField()
    paozhi = models.TextField()
    xingzhuang = models.TextField()
    xwgj = models.TextField()
    gnzz = models.TextField()
    pzzy = models.TextField()
    yfyl = models.TextField()
    zc = models.TextField()
    syzy = models.TextField()
    ckzl = models.TextField()


class QSHistory(models.Model):
    question = models.TextField()
    ans = models.TextField()
    satisfy = models.IntegerField(default=1)
    user = models.CharField(max_length=20, default='未登录')
