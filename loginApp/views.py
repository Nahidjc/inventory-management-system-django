from django.shortcuts import render
from loginApp.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def adminLogin(request):
    form = UserLoginForm()
    error = ''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(username, password)
            if user is not None:
                login(request, user)
                return redirect('/transaction/item-dashboard/')
            else:
                error = 'Invalid username or password'
            # A backend authenticated the credentials
        else:
            error = 'Invalid username or password'

    return render(request, 'loginApp/login.html', context={'form': form, 'error': error})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('/transaction/item-dashboard/')
