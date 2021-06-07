from django.db import models
from django.contrib.auth.models import User
from django.forms.models import modelform_factory

# Create your models here

class Owner(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)


class Category(models.Model):
    name = models.CharField(unique = True, max_length = 50)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=500)
    media = models.FileField(upload_to='pics', max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.ManyToManyField(Category, through='AnnounCategory', related_name='category')


    def __str__(self):
        return f'{self.title.title()}: {self.text[:300]}'



class AnnounCategory(models.Model):
    advert = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Response(models.Model):
    advert = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=255)
    response_datetime = models.DateTimeField(auto_now_add=True)





