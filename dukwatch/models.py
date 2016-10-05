from django.db import models

# Create your models here.
class Post_sample(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)
    def __str__(self):
        return self.title

class VideoBoard(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    Day = models.DateTimeField(auto_created=True, auto_now=True)
    URL = models.CharField(max_length=100)
    UserName = models.CharField(max_length=20)
    popular = models.CharField(max_length=10)
    New = models.CharField(max_length=10)

class Free_Board(models.Model) :
    title = models.CharField(max_length=100)