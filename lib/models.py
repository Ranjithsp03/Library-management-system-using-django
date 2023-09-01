from django.db import models

# Create your models here.
class admin1(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)

class book(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    booktitle=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    booknumber=models.CharField(max_length=100)
    pubdate=models.CharField(max_length=100)
    qty=models.IntegerField()
    status=models.BooleanField()

class student(models.Model):
    studentid=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    contactadd=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    studentpassword=models.CharField(max_length=100)

class bookt(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    bid=models.ForeignKey(book,on_delete=models.CASCADE)
    sid=models.ForeignKey(student,on_delete=models.CASCADE)