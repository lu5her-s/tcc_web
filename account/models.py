from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# NOTE : class For sector creation
class Sector(models.Model):
    ''' This class for sector '''
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
# NOTE : class for rank
class Rank(models.Model):
    ''' This class for create rank for user '''
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
# NOTE : class for position  ตำแหน่งของ user
class Position(models.Model):
    ''' for position of user'''
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

# NOTE : class for create new profile
class Profile(models.Model):
    ''' create user profile '''
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    rank     = models.ForeignKey(Rank, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    sector   = models.ForeignKey(Sector, on_delete=models.CASCADE, blank=True, null=True)
    place    = models.CharField(max_length=200, blank=True, null=True)
    phone    = models.CharField(max_length=10, blank=True, null=True)
    image    = models.ImageField(upload_to='Profile/', blank=True, null=True)
    
    # REVIEW : make return refer
    def __str__(self) -> str:
        if self.rank:
            return self.rank.name + self.user.get_full_name() 
        else:
            return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
    
# REVIEW ; update for token line
class LineToken(models.Model):
    ''' add Line token for send line notify '''
    name  = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    note  = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
