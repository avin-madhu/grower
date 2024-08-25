from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# the models parameter is what set's it apart from being a normal class and to a django table
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # Basically a text filed
    name = models.CharField(max_length=200)
    # bascially can be left blank or not have a value initially
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    #only saves the ate only when we create unlike auto_now which does it every time we save
    created = models.DateTimeField(auto_now_add=True)

    # set the newest created rooms to be on the top ( if last remove the '-')
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # if a room gets deleted we just want to delete all the messages associated with it.
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    