# --------CREATE REGISTRATION FORM--------

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import mahak
def myfun(request):
   if request.method=='POST':
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    data=mahak.objects.create(name=name,email=email,phone=phone)
    data.save()
    return redirect('read')
   else:    
    return render(request,'vivan.html')
   
#--------DETAIL READ OPERATION--------

def read(request):
  data=mahak.objects.all()
  return render(request,'read.html',{'data':data})   


#--------DELETE OPERATION--------------

def delete(request,id):
  data=mahak.objects.get(id=id)
  data.delete()
  return redirect('read')


#-------EDIT OPERATION----------------


def edit(request,id):
  data=mahak.objects.get(id=id)
  data.genre="pop"
  data.save()
  return redirect('read')

 
















