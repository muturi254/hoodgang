from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=30)
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    occupants_count = models.PositiveIntegerField(default=0)
    hood_location = models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=3)    
    last_name = models.CharField(max_length=3)    
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbourhood')
    birth_date = models.DateTimeField(null=True, blank=True)


class Business(models.Model):
    business_name = models.CharField(max_length=30)
    business_email = models.EmailField()
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    buiness_location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
