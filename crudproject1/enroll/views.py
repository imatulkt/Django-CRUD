from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

#This function will add and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ca = fm.cleaned_data['calorie']
            fa = fm.cleaned_data['fat']

            reg = User(name=nm, calorie=ca, fat=fa)
            reg.save()
            

    else:
        fm = StudentRegistration()
    
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

#This function will edit the data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})




    #This function will delete 
def delete_data(request, id):
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')

