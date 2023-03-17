from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# Create user manager class for custom user model
class UserManager(BaseUserManager):
    # create user
    def create_user(self, email, password, **extra_fields):
        # check if email is provided
        if not email:
            raise ValueError(_('Email is required'))
        # normalize email
        email = self.normalize_email(email)
        # create user
        user = self.model(email=email, **extra_fields)
        # set password
        user.password = make_password(password)
        # save user
        user.save()
        # return user
        return user

    # create superuser
    def create_superuser(self, email, password, **extra_fields):
        # set is_staff and is_superuser to True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # check if is_staff is True
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        # check if is_superuser is True
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        # return create user
        return self.create_user(email, password, **extra_fields)
    
# Create custom user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    # set email as username field
    USERNAME_FIELD = 'email'
    # set required fields
    REQUIRED_FIELDS = []
    # set user manager
    objects = UserManager()

    # get full name
    def get_full_name(self):
        # return first name and last name
        return f'{self.first_name} {self.last_name}'
    
    # get short name
    def get_short_name(self):
        # return first name
        return self.first_name
    
    # set __str__ method
    def __str__(self):
        return self.email
    
    # set __repr__ method
    def __repr__(self):
        return f'<User: {self.email}>'
    
    # set meta class
    class Meta:
        # set verbose name
        verbose_name = _('user')
        # set verbose name plural
        verbose_name_plural = _('users')
        # set ordering
        ordering = ('-date_joined',)

# Create user profile model

class Profile(models.Model):
    # set one to one relationship with user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # set profile picture
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True, null=True)
    # set bio
    bio = models.TextField(_('bio'), blank=True)
    # set birth date
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    # set phone number
    phone_number = models.CharField(_('phone number'), max_length=20, blank=True)
    # set website
    website = models.URLField(_('website'), blank=True)
    # set address
    address = models.CharField(_('address'), max_length=255, blank=True)
    # set city
    city = models.CharField(_('city'), max_length=150, blank=True)
    # set country
    country = models.CharField(_('country'), max_length=150, blank=True)
    # set created at
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    # set updated at
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    # set __str__ method
    def __str__(self):
        # return user email
        return self.user.email
    
    # set __repr__ method
    def __repr__(self):
        # return user email
        return f'<Profile: {self.user.email}>'
    
    # set meta class
    class Meta:
        # set verbose name
        verbose_name = _('profile')
        # set verbose name plural
        verbose_name_plural = _('profiles')
        # set ordering
        ordering = ('-created_at',)