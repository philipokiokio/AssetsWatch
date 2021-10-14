from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from .managers import UserManager
from django.utils.text import slugify
import uuid
import jwt
from datetime import datetime, timedelta
from django.conf import settings



# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'),default='none', max_length=20, unique=True)
    email = models.EmailField(_('email address'), unique= True)
    full_name = models.CharField(_('full name'), max_length= 60, blank=True, null=True)
    slug = models.SlugField(default='none',blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    
    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
        user_name = self.username
        user_id = str(uuid.uuid4())
    
        sluger = f'{user_name}-{user_id[:5]}'
        self.slug = slugify(sluger)
        super(User,self).save(*args,**kwargs)
        

        
        
        


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    





  