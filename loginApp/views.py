from django.shortcuts import render
from loginApp.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def adminLogin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
            # A backend authenticated the credentials

    return render(request, 'loginApp/login.html', context={'form': form})


def logoutUser(request):
    logout(request)
