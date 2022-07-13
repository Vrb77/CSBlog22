from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    bid=models.AutoField(primary_key=True)
    aname=models.CharField(max_length=50)
    btitle=models.CharField(max_length=250)
    desc=models.CharField(max_length=2000)
    date=models.DateField()
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="display")

class Comment(models.Model):
    cid=models.AutoField(primary_key=True)
    cbody=models.CharField(max_length=250)
    bcid=models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="comm")

class Feedback(models.Model):
    fid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="")
    email=models.CharField(max_length=20,default="")
    suggestions=models.CharField(max_length=150,default="")