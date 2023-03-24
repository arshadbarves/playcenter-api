from django.urls import path
from . import views

urlpatterns = [
    # path for welcome
    path('', views.WelcomeAPIView.as_view(), name='welcome'),
    # path for login
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    # path for create account
    path('register/', views.UserCreateAccountAPIView.as_view(), name='register'),
    # path for password change
    path('password/change/', views.UserChangePasswordAPIView.as_view(),
         name='password_change'),
    # path for password reset
    path('password/reset/', views.UserResetPasswordAPIView.as_view(),
         name='password_reset'),
    # path for password reset confirm
    path('password/reset/confirm/', views.UserResetPasswordConfirmAPIView.as_view(),
         name='password_reset_confirm'),
    # path for profile
    path('profile/', views.UserAPIView.as_view(), name='profile'),
    # path for profile edit
    path('profile/edit/', views.UserUpdateAPIView.as_view(), name='profile_edit'),
    # path for profile delete
    path('profile/delete/', views.UserDeleteAPIView.as_view(),
         name='profile_delete'),
    # path for logout
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
]
