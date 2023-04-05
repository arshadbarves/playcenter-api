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
        messages = []
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.append('Invalid username or password')
            return render(request, sign_in_template, {'messages': messages})

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
        messages = []
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        email = request.POST.get("email", None).lower()
        password = request.POST.get("password", None)
        password2 = request.POST.get("confirm_password", None)

        # Validate email addresses
        if not email:
            messages.append('Email is required')
            return render(request, create_account_template, {'messages': messages})

        # Validate user input
        if not first_name:
            messages.append('First name is required')
            return render(request, create_account_template, {'messages': messages})

        if not last_name:
            messages.append('Last name is required')
            return render(request, create_account_template, {'messages': messages})

        if not email:
            messages.append('Email is required')
            return render(request, create_account_template, {'messages': messages})

        if not password:
            messages.append('Password is required')
            return render(request, create_account_template, {'messages': messages})

        if not password2:
            messages.append('Confirm password is required')
            return render(request, create_account_template, {'messages': messages})

        if User.objects.filter(email=email).exists():
            messages.append('Email already exists')
            return render(request, create_account_template, {'messages': messages})

        if password != password2:
            messages.append('Passwords do not match')
            return render(request, create_account_template, {'messages': messages})

        user = User.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.append('Invalid username or password')
            return render(request, create_account_template, {'messages': messages})

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

# Callback View


class CallbackView(View):

    def get(self, request):
        # Get the code from the request
        code = request.GET.get('code', None)
        if code:
            authorized = True
            return render(request, 'account/callback.html', {'authorized': authorized})
        else:
            authorized = False
            return render(request, 'account/callback.html', {'authorized': authorized})
