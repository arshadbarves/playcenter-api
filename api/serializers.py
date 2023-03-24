from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from account import models


# User serializer
class UserSerializer(serializers.ModelSerializer):
    # Meta class
    class Meta:
        # set model
        model = models.User
        # set fields
        fields = ('id', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined')
        # set read only fields
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined')


# User login serializer
class UserLoginSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()
    # password
    password = serializers.CharField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get password
        password = data.get('password')
        # authenticate user
        user = authenticate(request=self.context.get(
            'request'), email=email, password=password)
        # check if user is authenticated
        if not user:
            # raise error
            raise serializers.ValidationError(_('Invalid credentials.'))
        # check if user is active
        if not user.is_active:
            # raise error
            raise serializers.ValidationError(_('User is not active.'))
        # set user
        data['user'] = user
        # return data
        return data


# User create account serializer


class UserCreateAccountSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()
    # password
    password = serializers.CharField()
    # password confirmation
    password_confirmation = serializers.CharField()
    # first name
    first_name = serializers.CharField()
    # last name
    last_name = serializers.CharField()
    # terms and conditions
    terms_and_conditions = serializers.BooleanField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get password
        password = data.get('password')
        # get password confirmation
        password_confirmation = data.get('password_confirmation')
        # get first name
        first_name = data.get('first_name')
        # get last name
        last_name = data.get('last_name')
        # get terms and conditions
        terms_and_conditions = data.get('terms_and_conditions')
        # check if email is already in use
        if models.User.objects.filter(email=email).exists():
            # raise error
            raise serializers.ValidationError(_('Email is already in use.'))
        # check if password and password confirmation are the same
        if password != password_confirmation:
            # raise error
            raise serializers.ValidationError(_('Passwords do not match.'))
        # check if terms and conditions are accepted
        if not terms_and_conditions:
            # raise error
            raise serializers.ValidationError(
                _('You must accept terms and conditions.'))
        # check if user is not already authenticated
        if self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(
                _('You are already authenticated.'))
        # return data
        return data

    # create
    def create(self, validated_data):
        # get email
        email = validated_data.get('email')
        # get password
        password = validated_data.get('password')
        # get first name
        first_name = validated_data.get('first_name')
        # get last name
        last_name = validated_data.get('last_name')
        # create user
        user = models.User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # send email verification email
        user.send_email_verification_email()
        # return user
        return user


# User update account serializer
class UserUpdateAccountSerializer(serializers.Serializer):
    # first name
    first_name = serializers.CharField()
    # last name
    last_name = serializers.CharField()

    # validate
    def validate(self, data):
        # get first name
        first_name = data.get('first_name')
        # get last name
        last_name = data.get('last_name')
        # check if user is authenticated
        if not self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(_('You are not authenticated.'))
        # return data
        return data

    # update
    def update(self, instance, validated_data):
        # get first name
        first_name = validated_data.get('first_name')
        # get last name
        last_name = validated_data.get('last_name')
        # set first name
        instance.first_name = first_name
        # set last name
        instance.last_name = last_name
        # save instance
        instance.save()
        # return instance
        return instance


# User change password serializer
class UserChangePasswordSerializer(serializers.Serializer):
    # old password
    old_password = serializers.CharField()
    # new password
    new_password = serializers.CharField()
    # new password confirmation
    new_password_confirmation = serializers.CharField()

    # validate
    def validate(self, data):
        # get old password
        old_password = data.get('old_password')
        # get new password
        new_password = data.get('new_password')
        # get new password confirmation
        new_password_confirmation = data.get('new_password_confirmation')
        # check if user is authenticated
        if not self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(_('You are not authenticated.'))
        # check if old password is correct
        if not self.context.get('request').user.check_password(old_password):
            # raise error
            raise serializers.ValidationError(
                _('Old password is not correct.'))
        # check if new password and new password confirmation are the same
        if new_password != new_password_confirmation:
            # raise error
            raise serializers.ValidationError(_('Passwords do not match.'))
        # return data
        return data

    # update
    def update(self, instance, validated_data):
        # get new password
        new_password = validated_data.get('new_password')
        # set new password
        instance.set_password(new_password)
        # save instance
        instance.save()
        # return instance
        return instance


# User reset password serializer
class UserResetPasswordSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # check if user is authenticated
        if self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(
                _('You are already authenticated.'))
        # check if email is not in use
        if not models.User.objects.filter(email=email).exists():
            # raise error
            raise serializers.ValidationError(_('Email is not in use.'))
        # return data
        return data

    # create
    def create(self, validated_data):
        # get email
        email = validated_data.get('email')
        # get user
        user = models.User.objects.get(email=email)
        # send reset password email
        user.send_reset_password_email()
        # return user
        return user


# User reset password confirm serializer
class UserResetPasswordConfirmSerializer(serializers.Serializer):
    # new password
    new_password = serializers.CharField()
    # new password confirmation
    new_password_confirmation = serializers.CharField()

    # validate
    def validate(self, data):
        # get new password
        new_password = data.get('new_password')
        # get new password confirmation
        new_password_confirmation = data.get('new_password_confirmation')
        # check if user is authenticated
        if self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(
                _('You are already authenticated.'))
        # check if new password and new password confirmation are the same
        if new_password != new_password_confirmation:
            # raise error
            raise serializers.ValidationError(_('Passwords do not match.'))
        # return data
        return data

    # update
    def update(self, instance, validated_data):
        # get new password
        new_password = validated_data.get('new_password')
        # set new password
        instance.set_password(new_password)
        # save instance
        instance.save()
        # return instance
        return instance


# User email verification serializer
class UserEmailVerificationSerializer(serializers.Serializer):
    # key
    key = serializers.CharField()

    # validate
    def validate(self, data):
        # get key
        key = data.get('key')
        # check if user is authenticated
        if self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(
                _('You are already authenticated.'))
        # check if key is not valid
        if not models.User.objects.filter(email_verification_key=key).exists():
            # raise error
            raise serializers.ValidationError(_('Key is not valid.'))
        # return data
        return data

    # update
    def update(self, instance, validated_data):
        # get key
        key = validated_data.get('key')
        # get user
        user = models.User.objects.get(email_verification_key=key)
        # set email verified
        user.email_verified = True
        # save user
        user.save()
        # return user
        return user

# User Delete Account Serializer


class UserDeleteAccountSerializer(serializers.Serializer):
    # password
    password = serializers.CharField()

    # validate
    def validate(self, data):
        # get password
        password = data.get('password')
        # check if user is authenticated
        if not self.context.get('request').user.is_authenticated:
            # raise error
            raise serializers.ValidationError(_('You are not authenticated.'))
        # check if password is not correct
        if not self.context.get('request').user.check_password(password):
            # raise error
            raise serializers.ValidationError(_('Password is not correct.'))
        # return data
        return data

    # delete
    def delete(self, instance):
        # delete instance
        instance.delete()
        # return instance
        return instance
