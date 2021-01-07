from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


# Custom User Model Manager
class UserManager(BaseUserManager):
    # Creates and saves a User with the given phone_number and password.
    def create_user(self, username, phone_number, email, password, country_code='+880', name=None):

        # Check if user exists
        user = self.model.objects.filter(phone_number=phone_number,
                                         email=email,
                                         username=username,
                                         country_code=country_code)

        if user.exists():
            raise ValidationError('User already exists')
        # Creating user instance
        user = self.model(username=username,
                          email=self.normalize_email(email),
                          phone_number=phone_number,
                          country_code=country_code,
                          name=name)

        user.name = name
        # Set user password
        user.set_password(password)
        user.save(using=self._db)
        return user

        # Creates staff user

    def create_staffuser(self, username, phone_number, email, password, country_code='+1', name=None):
        # Creates a non super admin
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
            country_code=country_code
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    # Creates Admin
    def create_superuser(self, username, phone_number, email, password, country_code='+1', name=None):
        # Creates and saves a superuser with the given email and password.
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
            country_code=country_code
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
