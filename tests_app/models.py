from django.db import models

from .public_id import encode


class Test(models.Model):
    slug = models.SlugField(db_index=True, unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='test_imgs')


class Option(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='test_imgs')
    test = models.ForeignKey(Test, related_name='options')


class FacebookUser(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=150)
    access_token = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    birthday = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


class TestAnswer(models.Model):
    public_id = models.CharField(max_length=10, unique=True, db_index=True)
    user = models.ForeignKey(FacebookUser)
    test = models.ForeignKey(Test)
    option = models.ForeignKey(Option)
