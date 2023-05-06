from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    

    return render(request,'home.html')


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'UFO':ufo,'PFO':pfo}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            user_non_save=UFD.save(commit=False)
            user_non_save.set_password(UFD.cleaned_data['password'])
            user_non_save.save()

            profile_non_save=PFD.save(commit=False)
            profile_non_save.username=user_non_save
            profile_non_save.save()

            send_mail('this is my project mail',
                      "hai how are you em chestunav call chey",
                      'vinayhampi31@gmail.com',
                      [user_non_save.email],
                      fail_silently=False

                      )

            return HttpResponse('registration sucessfully')
        else:
            return HttpResponse('in')
   
      
    return render(request,'registration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('password and user name wrong') 
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    



