from django.urls import path
from . import views

urlpatterns = [
    # path for welcome
    path('home/', views.WelcomeView.as_view(), name='home'),
    # path for login
    path('signin/', views.LoginView.as_view(), name='signin'),
    # path for registration
    path('createaccount/', views.CreateAccountView.as_view(), name='create account'),
    # # path for password change
    # path('password/change/', views.UserPasswordUpdateView.as_view(),
    #      name='password_change'),
    # path for password reset
    path('password/reset/', views.UserPasswordResetView.as_view(),
         name='password_reset'),
    # path for password reset confirm
    path('password/reset/confirm/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # # path for profile
    # path('profile/', views.UserView.as_view(), name='profile'),
    # # path for profile edit
    # path('profile/edit/', views.UserUpdateView.as_view(), name='profile_edit'),
    # # path for profile delete
    # path('profile/delete/', views.UserDeleteView.as_view(),
    #      name='profile_delete'),
    # # path for logout
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # path for callback
    path('callback/', views.CallbackView.as_view(), name='callback'),
]
