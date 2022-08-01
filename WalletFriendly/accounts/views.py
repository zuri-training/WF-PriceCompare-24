from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # Redirect to a success page.
        else:
            message.success(
                request, ("There was and error logging in, try again"))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
