from django.db import models

# Create your models here.
class Post_sample(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)
    def __str__(self):
        return self.title

class Video_Board(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    Day = models.DateTimeField(auto_created=True, auto_now=True)
    URL = models.CharField(max_length=100)
    UserName = models.CharField(max_length=20)
    popular = models.CharField(max_length=10)
    New = models.CharField(max_length=10)

class Ranking_Board(models.Model) :
    Ranking = models.IntegerField(max_length=1000)
    Title = models.CharField(max_length=100)
    UserName = models.CharField(max_length=20)
    Point = models.CharField(max_length=5)
    Char =  models.CharField(max_length=10)
    PlayTime = models.CharField(max_length=5)
    KillDet = models.CharField(max_length=10)
    mostchar = models.CharField(max_length=10)
    KillDeath = models.CharField(max_length=10)
    Tier = models.CharField(max_length=10)

class Character(models.Model) :
    userNo = models.IntegerField()
    type = models.IntegerField() #1->경쟁전, 2-> 빠른대전
    characterName = models.CharField(max_length=100) # 캐릭터 명이 들어감
    kd = models.FloatField()


class User_data(models.Model) :
    Name = models.CharField(max_length=10)
    Tier = models.CharField(max_length=10)
    KillDeath = models.CharField(max_length=10)
    Character = models.CharField(max_length=10)



class Free_Board(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    Day = models.DateTimeField(auto_created=True, auto_now=True)
    UserName = models.CharField(max_length=20)

