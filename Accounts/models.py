from django.core.exceptions import PermissionDenied
from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
from Accounts.manager import UserManager


def user_has_perm(user, perm, obj):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


def user_has_module_perms(user, app_label):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_module_perms'):
            continue
        try:
            if backend.has_module_perms(user, app_label):
                return True
        except PermissionDenied:
            return False
    return False


class User(AbstractBaseUser, PermissionsMixin):
    # Name / User name
    username = models.CharField(max_length=128,
                                editable=True,
                                null=False,
                                blank=False,
                                unique=True)
    # Phone Number
    phone_number = models.CharField(max_length=17,
                                    verbose_name='Phone Number',
                                    editable=True)
    # Country Code
    country_code = models.CharField(max_length=6,
                                    verbose_name='Phone number country code',
                                    default='+880',
                                    null=False,
                                    blank=False)

    name = models.CharField(max_length=220, verbose_name="Full Name", blank=True, null=True)

    # Email
    email = models.EmailField(editable=True, unique=True)

    # Stripe id for user

    # is the user active or not
    active = models.BooleanField(default=True)
    # a admin user; non super-user
    staff = models.BooleanField(default=False)
    # a superuser
    admin = models.BooleanField(default=False)
    # Account Creation Time
    created = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone_number', 'country_code']

    # calling user manager class
    objects = UserManager()

    class Meta:
        unique_together = ['phone_number', 'country_code']

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active admin have all permissions.
        if self.admin:
            return True

        # Otherwise we need to check the backends.
        return user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        # User permission to view
        if self.admin:
            return True
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active admin have all permissions.
        if self.admin:
            return True

        return user_has_module_perms(self, app_label)

    @property
    def is_staff(self):
        # Returns true if user is staff
        return self.staff

    @property
    def is_admin(self):
        # returns true if user is admin or not
        return self.admin

    @property
    def is_active(self):
        # returns true if user is active or not
        return self.active

