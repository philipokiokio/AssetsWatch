from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.

User = get_user_model()


class Asset(models.Model):

    TRADE_HOLD_CHOICE =[
        ('TRADE', 'Trade'),
        ('HOLD', 'Hold')
    ]



    name = models.CharField(max_length=15, help_text='Name of the asset owned')
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    price_at_buy = models.FloatField(max_length=10, help_text='Price at which each asset is bought')
    currency_medium = models.CharField(max_length=6, help_text='Currency used to pay for the asset.')
    currency_bought = models.CharField(max_length=7, help_text='The asset bought')
    wallet_id = models.CharField(max_length=30, null=True, blank=True, help_text='')
    gas_price_paid = models.FloatField(max_length= 9,null=True, blank=True,help_text='fees charged for asset bought')
    date_bought = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True, help_text= 'The date when the asset was bought')
    gains_losses = models.FloatField(validators=[MinLengthValidator(0),MaxLengthValidator(100)], null=True, blank= True)
    sold= models.BooleanField(False)
    trade_hold = models.CharField(max_length=6, choices= TRADE_HOLD_CHOICE,default= 'HOLD')
    date_added = models.DateTimeField(auto_now_add=True, help_text='date added to assetwatch')
    update_date = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name

    class Meta:
        verbose_name = 'asset'
        verbose_name_plural = 'assets'
    
    
