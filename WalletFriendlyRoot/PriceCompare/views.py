from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import CreateProfile
# Create your views here.


def index(request):
    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user exist
            login(request, user)
            messages.success(request, ('Youre logged in'))
            return redirect('index')  # routes to 'home' on successful login
        else:
            messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})


def signup(request):
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
    return render(request, 'registration/signup.html', context)


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
    return render(request, 'registration/forgotPassword.html', context)


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
