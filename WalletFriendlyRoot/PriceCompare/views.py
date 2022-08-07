import email
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'base.html')
    
@login_required
def login(request):
    return render(request, 'registration/login.html',)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/Signup.html',{'form':form} )

def forgotpassword(request):
    return render(request, 'registration/forgotPassword.html')

def fashion(request):
    return render(request, 'fashion/fashion.html')

def fashionmen(request):
    return render(request, 'fashion/fashionMen.html')
    
def fashionwomen(request):
    return render(request, 'fashion/fashionWomen.html')

def gadgets(request):
    return render(request, 'gadget/gadgetHompage.html')

def laptop(request):
    return render(request, 'gadget/gadgetLaptops.html')

def phone(request):
    return render(request, 'gadget/gadgetPhones.html')

def tv(request):
    return render(request, 'gadget/gadgettv.html')

def hair(request):
    return render(request, 'hair/hairHomePage.html')

def bonestraight(request):
    return render(request, 'hair/boneStraight.html')

def accessories(request):
    return render(request, 'hair/hairAccessories.html')
    
def humanhair(request):
    return render(request, 'hair/humanHair.html')

