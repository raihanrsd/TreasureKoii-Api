from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import AbstractUser
from managers import UserManager

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    phone_number= models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Hunt(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    poster_img = models.ImageField(upload_to='images/', blank=True)
    
    # Once user will create a hunt but after that, he/she can add other users as organizers
    organizers = models.ManyToManyField(User, related_name='organizers')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Hunt, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
