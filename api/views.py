from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from api import serializers
from account import models

# Welcome API View


class WelcomeAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        # return response
        return Response(
            data={
                'message': 'You are accessing the Playcenter API'
            },
            status=status.HTTP_200_OK
        )

# User API View


class UserAPIView(generics.RetrieveAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)
    # serializer class
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        return self.request.user

# User Create Account API View


class UserCreateAccountAPIView(generics.CreateAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)
    # serializer class
    serializer_class = serializers.UserCreateAccountSerializer

    def create(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # create user
        user = models.User.objects.create_user(**validated_data)
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


# User login API view
class UserLoginAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)
    # serializer class
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
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


# User logout API view
class UserLogoutAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # get token
        token = request.auth
        # delete token
        token.delete()
        # return response
        return Response(
            data={
                'message': 'You have been logged out successfully.'
            },
            status=status.HTTP_200_OK
        )


# User API view
class UserAPIView(generics.RetrieveAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)
    # serializer class
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        return self.request.user


# User Update API view
class UserUpdateAPIView(generics.UpdateAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)
    # serializer class
    serializer_class = serializers.UserUpdateAccountSerializer

    def get_object(self):
        # get user
        return self.request.user

    def update(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = self.get_object()
        # update user
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )


# User Change Password API view
class UserChangePasswordAPIView(generics.UpdateAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)
    # serializer class
    serializer_class = serializers.UserChangePasswordSerializer

    def get_object(self):
        # get user
        return self.request.user

    def update(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = self.get_object()
        # update user
        user.set_password(validated_data['password'])
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )


# User Delete API view
class UserDeleteAPIView(generics.DestroyAPIView):
    # permission classes
    permission_classes = (permissions.IsAuthenticated,)
    # serializer class
    serializer_class = serializers.UserSerializer

    def get_object(self):
        # get user
        return self.request.user

    # delete
    def delete(self, request, *args, **kwargs):
        # get user
        user = self.get_object()
        # delete user
        user.delete()
        # return response
        return Response(
            data={
                'message': 'Your account has been deleted successfully.'
            },
            status=status.HTTP_200_OK
        )

# User Reset Password API view


class UserResetPasswordAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)
    # serializer class
    serializer_class = serializers.UserResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # set password
        user.set_password(validated_data['password'])
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )


# User Reset Password Confirm API view
class UserResetPasswordConfirmAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)
    # serializer class
    serializer_class = serializers.UserResetPasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # set password
        user.set_password(validated_data['password'])
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )


# User Verify Email API view
class UserVerifyEmailAPIView(generics.GenericAPIView):
    # permission classes
    permission_classes = (permissions.AllowAny,)
    # serializer class
    serializer_class = serializers.UserEmailVerificationSerializer

    def post(self, request, *args, **kwargs):
        # get serializer
        serializer = self.serializer_class(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        # get validated data
        validated_data = serializer.validated_data
        # get user
        user = validated_data['user']
        # set is_verified
        user.is_verified = True
        user.save()
        # return response
        return Response(
            data=serializers.UserSerializer(user).data,
            status=status.HTTP_200_OK
        )
