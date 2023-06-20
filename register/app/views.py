from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.views.generic import (TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView,)
from django.contrib.auth.forms import UserCreationForm
from app.forms import signupform

# Create your views here

def signupview(request):

    if request.method == "POST" :
        form = signupform(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login')
    else:
       form = signupform()
    return render(request,'signup.html',{'form':form})

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username,password=password)
        if user is not None:
            login(request,user)
            return render('next')
    else:

        return render(request,'login.html')
        
def next(request):
    return render(request,'next.html')