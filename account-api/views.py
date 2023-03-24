from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from ..api import serializers
from . import models
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Welcome view
class WelcomeView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        # return response
        return Response(
            data={
                'message': 'Welcome to the API.'
            },
            status=status.HTTP_200_OK
        )

# Callback view


class CallbackView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print(request)
        # Get the url parameters
        code = request.GET.get('code')
        if (code == None):
            authorized = False
        else:
            authorized = True
        print(code)
        # print(state)
        # return response
        return render(request, 'callback.html', {'authorized': authorized})


# User registration view
class UserRegistrationView(APIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserRegistrationSerializer

    def post(self, request):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # create user
        user = models.User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # create token
        token = Token.objects.create(user=user)
        # return response
        return Response(
            data={
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            },
            status=status.HTTP_201_CREATED
        )

# User login view


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self, request):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # create token
        token, _ = Token.objects.get_or_create(user=user)
        # return response
        return Response(
            data={
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            },
            status=status.HTTP_200_OK
        )

# User logout view


class UserLogoutView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # get token
        request.user.auth_token.delete()
        # return response
        return Response(status=status.HTTP_204_NO_CONTENT)

# User view


class UserView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        user = self.request.user
        # return user
        return user

# User update view


class UserUpdateView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        user = self.request.user
        # return user
        return user

    def update(self, request, *args, **kwargs):
        # get user
        user = self.get_object()
        # get serializer
        serializer = self.serializer_class(user, data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # update user
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )

# User password update view


class UserPasswordUpdateView(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserPasswordChangeSerializer

    def get_object(self):
        # get user
        user = self.request.user
        # return user
        return user

    def update(self, request, *args, **kwargs):
        # get user
        user = self.get_object()
        # get serializer
        serializer = self.serializer_class(user, data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # update user password
        user.password = make_password(validated_data['password'])
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )

# User delete view


class UserDeleteView(generics.DestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        user = self.request.user
        # return user
        return user

    def destroy(self, request, *args, **kwargs):
        # get user
        user = self.get_object()
        # delete user
        user.delete()
        # return response
        return Response(status=status.HTTP_204_NO_CONTENT)

# User list view


class UserListView(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        # get users
        users = models.User.objects.all()
        # return users
        return users

# User password reset view


class UserPasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserPasswordResetSerializer

    def post(self, request):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # create token
        token = Token.objects.create(user=user)
        # return response
        return Response(
            data={
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            },
            status=status.HTTP_200_OK
        )

# User password reset confirm view


class UserPasswordResetConfirmView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserPasswordResetConfirmSerializer

    def post(self, request):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # update user password
        user.password = make_password(validated_data['password'])
        user.save()
        # return response
        return Response(status=status.HTTP_200_OK)
