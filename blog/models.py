from django.db import models

# Create your models hee.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)

    def __str__(self):
        return self.title
