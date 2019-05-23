from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)
    sex = models.CharField(max_length=30, default="null")
    age = models.IntegerField(default=0)
    occupation  = models.CharField(max_length=200, default="null")
    zipcode = models.CharField(max_length=30, default="null")


class Item(models.Model):
    item_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=200, default="null")
    genre = models.CharField(max_length=30, default="null")


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    timestamp = models.CharField(max_length=30, default="null")


class Paper(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=1000, default="")
    intro = models.CharField(max_length=3000, default="")
    content = models.CharField(max_length=30000, default="")
    timeCreated = models.CharField(max_length=30, default="")
