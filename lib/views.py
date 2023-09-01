from django.http import   HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
import datetime
# Create your views here.
def alogin(request):
    if request.method=="GET":
        return render(request,"Alogin.html")
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        data=admin1.objects.filter(name=name,passwd=password)
        if data:
            return HttpResponseRedirect(reverse("bookdis"))
    return render(request,"Alogin.html")
def bookdis(request):
    if request.method=="GET":
        return render(request,"bookdis.html",{
                    "data":book.objects.all()
                })
def bookadd(request):
    if request.method=="GET":
        return render(request,"bookadd.html")
    if request.method=="POST":
        booktitle=request.POST["booktitle"]
        bookname=request.POST["bookname"]
        publisher=request.POST["publisher"] 
        author=request.POST["author"]
        booknumber=request.POST["booknumber"]
        no=request.POST["number"]
        pubdate=request.POST["pubdate"]
        ob1=book.objects.create(booktitle=booktitle,bookname=bookname,publisher=publisher,author=author,booknumber=booknumber,pubdate=pubdate,qty=no,status=True)
        book.save(ob1)
        return HttpResponseRedirect(reverse("bookdis"))

def studentadd(request):
    if request.method=="GET":
        return render(request,"studentadd.html")
    if request.method=="POST":
        name=request.POST["name"]
        gender=request.POST["gender"]
        age=request.POST["age"] 
        email=request.POST["email"]
        contactadd=request.POST["contactadd"]
        studentpassword=request.POST["studentpassword"]
        ob1=student.objects.create(name=name,gender=gender,age=age,contactadd=contactadd,email=email,studentpassword=studentpassword)
        student.save(ob1)
        return HttpResponseRedirect(reverse("bookdis"))
def slogin(request):
    if request.method=="GET":
        return render(request,"slogin.html")
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        data=student.objects.filter(name=name,studentpassword=password)
        if data:
            return render(request,"shome.html",{
                "data":bookt.objects.filter(sid=data[0]),
                "id":data[0].studentid
            })
    return render(request,"slogin.html")
def borrow(request,sid):
    if request.method=="GET":
        return render(request,"borrow.html",{
            "data":book.objects.filter(status=True),
            "sid":sid
        })
def bbook(request,sid,bid):
    if request.method=="GET":
        ob=book.objects.get(id=bid)
        if ob.qty-1>=0:
            ob.qty-=1
            ob1=bookt.objects.create(bid=ob,sid=student.objects.get(studentid=sid))
            bookt.save(ob1)
        ob.save()
        return HttpResponseRedirect(reverse('slogin'))
def retur(request,id):
    if request.method=="GET":
        ob=bookt.objects.get(id=id)
        ob1=ob.bid
        ob1.qty+=1
        ob1.save()
        ob.delete()
    return HttpResponseRedirect(reverse('slogin'))
def studentdis(request):
    if request.method=="GET":
        return render(request,"studentdispaly.html",{
            "data":student.objects.all(),
        })