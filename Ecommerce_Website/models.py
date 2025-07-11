from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

# Create Customet profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=10, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)



class contactUs(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=500)
    objet = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contact Us'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone  = models.CharField(max_length=10)
    mail = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = 'Client'
    
    
    
class categories(models.Model):
    name_cat = models.CharField(max_length=100)
    img_cat = models.ImageField(upload_to='categorie/',blank=True)

    def __str__(self):
        return self.name_cat
    
    class Meta:
        verbose_name_plural = 'Categories'


class produit(models.Model):
    DISPO_CHOICES = [
        ('DISPO', 'DISPONIBLE'),
        ('REP', 'RUPTURE DE STOCK'),
        ('SALE', 'SALE'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8) 
    categorie = models.ForeignKey(categories, on_delete=models.CASCADE, default=1)  # Par défaut, une catégorie
    description = models.TextField()  # Use TextField for descriptions
    dispo = models.CharField(max_length=6, choices=DISPO_CHOICES, default='DISPO')
    image1 = models.ImageField(upload_to='produit/')
    image2 = models.ImageField(upload_to='produit/', blank=True, null=True)
    image3 = models.ImageField(upload_to='produit/', blank=True, null=True)
    image4 = models.ImageField(upload_to='produit/', blank=True, null=True)
    # Add Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6) 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Produit et Service'
    
    

class Order(models.Model):
    product = models.ForeignKey(produit, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status =  models.BooleanField(default=False)

    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name_plural = 'Commandes'

