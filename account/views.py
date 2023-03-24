import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from account.models import User
from playcenter_api import settings


login_template = 'account/login.html'
register_template = 'account/register.html'

api_url = settings.API_URL + 'login/'

# Welcome View


class WelcomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'account/home.html', {'user': request.user})
        else:
            return redirect('login')


# Login View


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, login_template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(api_url, data=data)
        if response.status_code == 200:
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, login_template, {'error': 'Invalid username or password'})

# Logout View


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('home')

# Create Account View


class CreateAccountView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, register_template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        data = {
            'username': username,
            'password': password,
            'email': email,
            'first_name': first_name,
            'last_name': last_name
        }
        response = requests.post(api_url, data=data)
        if response.status_code == 201:
            user = User.objects.create_user(**data)
            login(request, user)
            return redirect('home')
        else:
            return render(request, register_template, {'error': 'Invalid username or password'})
