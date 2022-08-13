from django.shortcuts import render, redirect
import requests
import json
from .forms import EmailForm
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.conf import settings
import smtplib
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import CreateProfile

# Create your views here.
def index(request):
    return render(request, 'index.html')
def indexauth(request):
    return render(request, 'indexAuth.html')

def login(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user exist
            login(request, user)
            messages.success(request, ('Youre logged in'))
            return redirect('login')  # routes to 'home' on successful login
        else:
            messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('login')
    else:
        return render(request, 'registration/Login.html')

def logout_user(request):
        logout(request)
        messages.success(request,('Youre now logged out'))
        return redirect('home')

def createaccount(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Youre now registered'))
            return redirect(request, 'registration/login.html')
        else:
            form = CreateProfile()
            context = {'form': form}
    return render(request, 'registration/createAccount.html')

def documentation(request):
    return render(request, 'documentation.html')

def forgotpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password'))
            return redirect('home')
    else:  # passes in user information
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'registration/forgotPassword.html')

def fashion(request):
    return render(request, 'fashion/fashion.html')

def fashionmen(request):
    return render(request, 'fashion/fashionMen.html')

def fashionmenauth(request):
    return render(request, 'fashion/fashionMenAuth.html')
    
def fashionwomen(request):
    return render(request, 'fashion/fashionWomen.html')

def fashionwomenauth(request):
    return render(request, 'fashion/fashionWomenAuth.html')

def gadget(request):
    return render(request, 'gadget/gadgetHomepage.html')

def laptop(request):
    return render(request, 'gadget/gadgetLaptops.html')

def laptopauth(request):
    return render(request, 'gadget/gadgetLaptopAuth.html')

def phones(request):
    return render(request, 'gadget/gadgetPhones.html')

def phoneauth(request):
    return render(request, 'gadget/gadgetPhonesAuth.html')

def tv(request):
    return render(request, 'gadget/gadgettv.html')

def tvauth(request):
    return render(request, 'gadget/gadgettvAuth.html')

def hair(request):
    return render(request, 'hair/hairHomePage.html')

def bonestraight(request):
    return render(request, 'hair/boneStraight.html')

def bonestraightauth(request):
    return render(request, 'hair/boneStraightAuth.html')

def accessories(request):
    return render(request, 'hair/hairAccessories.html')

def accessoriesauth(request):
    return render(request, 'hair/hairAccessoriesAuth.html')

def humanhair(request):
    return render(request, 'hair/humanHair.html')

def humanhairauth(request):
    return render(request, 'hair/humanhairAuth.html')

def comparegadget(request):
    return render(request, 'compare/compareGadgets.html')

def trendingnews(request):
    return render(request, 'trendingNews.html')

def review(request):
    return render(request, 'review.html')

def contactus(request):
    return render(request, 'contactUs.html')

def aboutus(request):
    return render(request, 'AboutUs.html')

def faq(request):
    return render(request, 'faq.html')

def hotdeals(request):
    return render(request, 'Hotdeals.html')

def team(request):
    return render(request, 'team.html')

# def home(request):

#     url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

#     querystring = {"name":"iphone  13"}

#     headers = {
# 	"X-RapidAPI-Key": "a2f30a74edmsh935c85c0c29ad8bp1c7557jsnc992726fee2b",
# 	"X-RapidAPI-Host": "magic-aliexpress1.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     data= response.json()

#     return render(request, "home.html",{'data':data['docs'][0],})

def sendMail(request):
        # check if form has been submitted
    if request.method == 'GET':
         form = EmailForm()
    else:
        form = EmailForm(request.POST)
        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            name=cd['name']
            subject = "Inquiry from a customer"
            message = cd['message']
            Email=cd['email']
            #form = EmailForm(request.POST)
        try:
            send_mail(subject, message, Email, ['walletfriendlyofficial@gmail.com',])
        except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('success')

    return render(request, 'contactUs.html', {
        'form': form,
        #'messageSent': messageSent,
    })

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

