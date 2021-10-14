from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True



    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username)
        user.set_password(password)
        user.is_superuser=False
        user.save()
        return user

    
    def create_superuser(self,email,username,password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username)
        user.set_password(password)      
        
        user.is_superuser=True
        user.is_staff=True

        if user.is_superuser is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return user