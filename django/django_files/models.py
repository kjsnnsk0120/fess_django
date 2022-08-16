from django.db import models
#import MySQLdb

# Create your models here.

class Data(models.Model):
    article = models.IntegerField()
    paragraph = models.IntegerField()
    content = models.TextField()

