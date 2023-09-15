from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# from dns import message

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error TRY AGAIN!")
            return redirect('home')

    else:  # in this case they are not posting any data means not logging in direct going home
        return render(request, 'home/index.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def register_user(request):
    return render(request, 'home/register.html')
