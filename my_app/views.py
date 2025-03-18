from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas

# Create your views here.
def home(request):
   myData=Datas.objects.all()
   if myData != '':

        return render(request,'index.html',{'myData':myData})

def addData(request):

    if request.method == 'POST':
        task = request.POST['task']

        myData = Datas()
        myData.Task = task 
        myData.save()

        return redirect('home')
    return render(request,'index.html')

def updateData(request,id):
    myData=Datas.objects.get(id=id)
    if request.method=='POST':
        task=request.POST['task']
        myData.Task=task
        myData.save()
        return redirect('home')
    return render(request,'upadte.html',{'myData':myData})


def deleteData(request,id):
    myData=Datas.objects.get(id=id)
    myData.delete()
    return redirect('home')