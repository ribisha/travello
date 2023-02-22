from django.db import models

class offer(models.Model):
    image=models.ImageField(upload_to="images")
    title=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()

class news(models.Model):
    image=models.ImageField(upload_to="images")
    day=models.IntegerField()
    month=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    desc=models.TextField()

class reg(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.TextField()
    pswd=models.CharField(max_length=30)


