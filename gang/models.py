from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=30, unique=True)
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    occupants_count = models.PositiveIntegerField(default=0)
    hood_location = models.CharField(max_length=30)

    def __str__(self):
        return self.hood_name

    @classmethod
    def create_neighbourhood(cls, hood_name, hood_location):
        hood = cls(hood_name=hood_name, hood_location=hood_location)
        hood.save()
        return hood

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        return cls.objects.get(id=neigborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True )    
    last_name = models.CharField(max_length=30, blank=True )    
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbourhood', null=True, blank=True )
    birth_date = models.DateField(null=True, blank=True)
    business = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    business_name = models.CharField(max_length=30)
    business_email = models.EmailField()
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    buiness_location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    post_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="post/pic/%Y-%m-%d", blank=True)
    post_body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.post_body
class contact(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    location = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
