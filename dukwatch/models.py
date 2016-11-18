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

class User_data(models.Model) :
    characterName = models.CharField(max_length=100)  # 캐릭터 명이 들어감
    UserName = models.CharField(max_length=20)
    Point = models.CharField(max_length=5)
    PlayTime = models.CharField(max_length=5)
    Level = models.IntegerField(max_length=5)

class Character_data(models.Model) :
    User = models.ForeignKey(User_data)
    type = models.IntegerField() #1->경쟁전, 2-> 빠른대전
    mostchar = models.CharField(max_length=10)
    Tier = models.CharField(max_length=10)
    WiningPer = models.CharField(max_length=10)
    kd = models.FloatField(max_length=10)
    runaway = models.timezone(max_length=10)
    sumrunaway = models.timezone(max_length=15)
    accuracy=models.CharField(max_length=10)
    medal=models.CharField(max_length=5)
    Gmedal = models.CharField(max_length=5)
    Smedal = models.CharField(max_length=5)
    Vmedal = models.CharField(max_length=5)
    Mission = models.timezone(max_length=10)
    BestMission = models.timezeon(max_length=10)
    MissionKill = models.IntegerField(max_length=10)
    BestMissionKill = models.IntegerField(max_length=5)
    score = models.IntegerField(max_lenth=5)
    Win = models.IntegerField(max_length=5)
    Lose = models.IntegerField(max_length=5)
    PiHaRang = models.IntegerField(max_length=10)
    Death = models.IntegerField(max_length=10)
    Deathave = models.FloatField(max_length=10)
    Critical = models.IntegerField(max_length=10)
    heal = models.IntegerField(max_length=20)
    Kill = models.IntegerField(max_length=15)
    SumKill = models.IntegerField(max_length=15)




class Free_Board(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    Day = models.DateTimeField(auto_created=True, auto_now=True)
    UserName = models.CharField(max_length=20)
