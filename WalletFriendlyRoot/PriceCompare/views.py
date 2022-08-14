from django.shortcuts import render, redirect
#import requests
#import json
from .forms import EmailForm
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.conf import settings
import smtplib
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm



# Create your views here.
def index(request):
    return render(request, 'index.html')
def indexauth(request):
    return render(request, 'indexAuth.html')

def login(request):
        return render(request, 'registration/Login.html')

def logout_user(request):
         return redirect('home')

def createaccount(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.username = form.cleaned_data.get('username')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.phone_number = form.cleaned_data.get('phone_number')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('indexauth')
    else:
        form = SignUpForm()
    return render(request, 'registration/createAccount.html', {'form': form})

def documentation(request):
    return render(request, 'documentation.html')

def forgotpassword(request):
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

