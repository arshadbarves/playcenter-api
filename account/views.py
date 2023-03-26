import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from account.models import User
from playcenter_api import settings


sign_in_template = 'account/signin.html'
create_account_template = 'account/createaccount.html'
home = settings.HOME_URL


# Welcome View


class WelcomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(home)
        else:
            return render(request, sign_in_template)


# Login View


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(home)
        else:
            return render(request, sign_in_template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, sign_in_template, {'error': 'Invalid username or password'})

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
            return render(request, create_account_template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, create_account_template, {'error': 'New user could not be created'})

# Password Reset View


class UserPasswordResetView(View):

    def get(self, request):
        return render(request, 'account/password_reset.html')

    def post(self, request):
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            return redirect('home')
        else:
            return render(request, 'account/password_reset.html', {'error': 'Passwords do not match'})

# Password Reset Confirm View


class UserPasswordResetConfirmView(View):

    def get(self, request):
        return render(request, 'account/password_reset_confirm.html')

    def post(self, request):
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            return redirect('home')
        else:
            return render(request, 'account/password_reset_confirm.html', {'error': 'Passwords do not match'})
