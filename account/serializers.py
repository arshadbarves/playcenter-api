from . import models
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

# User serializer
class UserSerializer(serializers.ModelSerializer):
    # Meta class
    class Meta:
        # set model
        model = models.User
        # set fields
        fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
        # set read only fields
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined')

# User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    # Meta class
    class Meta:
        # set model
        model = models.User
        # set fields
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        # set extra kwargs
        extra_kwargs = {'password': {'write_only': True}} # hide password field when returning data from API endpoint

    # create
    def create(self, validated_data):
        # get user
        user = models.User.objects.create_user(**validated_data)
        # return user
        return user
    
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
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        # check if user is authenticated
        if not user:
            # raise error
            raise serializers.ValidationError(_('Invalid email or password.'))
        # check if user is active
        if not user.is_active:
            # raise error
            raise serializers.ValidationError(_('User is deactivated.'))
        # set user
        data['user'] = user
        # return data
        return data

# User password change serializer
class UserPasswordChangeSerializer(serializers.Serializer):
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
        # check if new password and new password confirmation are the same
        if new_password != new_password_confirmation:
            # raise error
            raise serializers.ValidationError(_('New passwords do not match.'))
        # get user
        user = self.context.get('request').user
        # check if old password is correct
        if not user.check_password(old_password):
            # raise error
            raise serializers.ValidationError(_('Old password is incorrect.'))
        # set user
        data['user'] = user
        # return data
        return data

# User password reset serializer
class UserPasswordResetSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get user
        user = models.User.objects.filter(email=email).first()
        # check if user exists
        if not user:
            # raise error
            raise serializers.ValidationError(_('User does not exist.'))
        # set user
        data['user'] = user
        # return data
        return data
    
# User password reset confirm serializer
class UserPasswordResetConfirmSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()
    # old password
    old_password = serializers.CharField()
    # password
    password = serializers.CharField()
    # password confirmation
    password_confirmation = serializers.CharField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get old password
        old_password = data.get('old_password')
        # get password
        password = data.get('password')
        # get password confirmation
        password_confirmation = data.get('password_confirmation')
        # check if password and password confirmation are the same
        if password != password_confirmation:
            # raise error
            raise serializers.ValidationError(_('Passwords do not match.'))
        # get user
        user = models.User.objects.filter(email=email).first()
        # check if user exists
        if not user:
            # raise error
            raise serializers.ValidationError(_('User does not exist.'))
        # check if old password is correct
        if not user.check_password(old_password):
            # raise error
            raise serializers.ValidationError(_('Old password is incorrect.'))
        # set user
        data['user'] = user
        # return data
        return data

# User profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    # Meta class
    class Meta:
        # set model
        model = models.User
        # set fields
        fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
        # set read only fields
        read_only_fields = ('id', 'email', 'is_staff', 'is_active', 'date_joined')

# User profile edit serializer
class UserProfileEditSerializer(serializers.ModelSerializer):
    # Meta class
    class Meta:
        # set model
        model = models.User
        # set fields
        fields = ('id', 'email', 'first_name', 'last_name')
        # set read only fields
        read_only_fields = ('id', 'email')

# User profile change password serializer
class UserProfileChangePasswordSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()
    # password
    password = serializers.CharField()
    # password confirmation
    password_confirmation = serializers.CharField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get password
        password = data.get('password')
        # get password confirmation
        password_confirmation = data.get('password_confirmation')
        # check if password and password confirmation are the same
        if password != password_confirmation:
            # raise error
            raise serializers.ValidationError(_('Passwords do not match.'))
        # get user
        user = models.User.objects.filter(email=email).first()
        # check if user exists
        if not user:
            # raise error
            raise serializers.ValidationError(_('User does not exist.'))
        # set user
        data['user'] = user
        # return data
        return data
    
# User profile delete serializer
class UserProfileDeleteSerializer(serializers.Serializer):
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
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        # check if user is authenticated
        if not user:
            # raise error
            raise serializers.ValidationError(_('Invalid email or password.'))
        # check if user is active
        if not user.is_active:
            # raise error
            raise serializers.ValidationError(_('User is deactivated.'))
        # set user
        data['user'] = user
        # return data
        return data
    
# User profile delete confirm serializer
class UserProfileDeleteConfirmSerializer(serializers.Serializer):
    # email
    email = serializers.EmailField()

    # validate
    def validate(self, data):
        # get email
        email = data.get('email')
        # get user
        user = models.User.objects.filter(email=email).first()
        # check if user exists
        if not user:
            # raise error
            raise serializers.ValidationError(_('User does not exist.'))
        # set user
        data['user'] = user
        # return data
        return data