from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail

# Create your views here.
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


        return HttpResponse('invalid data')
        
    return render(request,'registration.html',d)
