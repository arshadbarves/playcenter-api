from django.urls import path
from . import views

urlpatterns = [
    # path for welcome
    path('', views.WelcomeView.as_view(), name='welcome'),
    # path for login
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path for registration
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path for password change
    path('password/change/', views.UserPasswordUpdateView.as_view(), name='password_change'),
    # path for password reset
    path('password/reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    # path for password reset confirm
    path('password/reset/confirm/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path for profile
    path('profile/', views.UserView.as_view(), name='profile'),
    # path for profile edit
    path('profile/edit/', views.UserUpdateView.as_view(), name='profile_edit'),
    # path for profile delete
    path('profile/delete/', views.UserDeleteView.as_view(), name='profile_delete'),
]
