from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_created')
    collaborators = models.ManyToManyField(User, related_name='events_collaborated', blank=True)

    def __str__(self):
        return self.name
