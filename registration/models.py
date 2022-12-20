from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Custom user manager...
class UserManager(BaseUserManager):

    def create_user(self, phone,name, password=None,password2=None):
        """Creates and saves a new user"""
        if not phone:
            raise ValueError('User must have an phone number')
        user = self.model(phone=phone,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone,name,password=None,password2=None):
        """creates and save a new super User"""
        user = self.create_user(phone=phone,name=name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """custom user model that supports using phone number of username"""
    phone = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'phone'


    def __str__(self):
        return self.phone


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True 

    @property  
    def is_staff(self):
        "Is the user a admin member?"
        return self.is_admin
