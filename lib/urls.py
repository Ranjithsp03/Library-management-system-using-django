from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.alogin,name="alogin"),
    path("bookdis/",views.bookdis,name="bookdis"),
    path("bookadd/",views.bookadd,name="bookadd"),
    path("student/",views.studentadd,name="studentadd"),
    path("slogin/",views.slogin,name="slogin"),
    path("borrow/<int:sid>/",views.borrow,name="borrow"),
    path("bbook/<int:sid>/<int:bid>/",views.bbook,name="bbook"),
    path("studentdisplay/",views.studentdis,name="studentdis"),
    path("retur/<int:id>",views.retur,name="retur"),
]