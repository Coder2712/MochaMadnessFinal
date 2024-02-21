from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15)

class Blogs(models.Model):
    image=models.ImageField(upload_to='image/')
    title= models.CharField(max_length=60)
    desc=models.CharField(max_length=2000)
    postby=models.CharField(max_length=20)                              # can also take TextField instead of CharField

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    desc=models.CharField(max_length=1000)

