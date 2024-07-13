from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import datas

#create your views here

def home(request):
    mydata=datas.objects.all()
    if (mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
       return render(request,"home.html")

def adddata(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        o=datas()
        o.Name=name
        o.Age=age
        o.Address=address
        o.Contact=contact
        o.Mail=mail
        o.save()
        mydata=datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

def updatedata(request,id):
    mydata=datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']


        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('home')
    return render(request,'update.html',{'data':mydata})

def deletedata(request,id):
    mydata=datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')