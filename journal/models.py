from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

def get_image_name(instance, filename):
    image_name = instance.journal.title
    return "JournalImage/{}/{}".format(image_name, filename)

def get_file_name(instance, filename):
    file_name = instance.journal.title
    return "JournalFile/{}/{}".format(file_name, filename)

class JournalType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class JournalStatus(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name        = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.name
    
# TODO : Make model class for Journal Record
class Journal(models.Model):
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journalAuthor')
    category   = models.ForeignKey(JournalType, on_delete=models.CASCADE, related_name='journalType')
    title      = models.CharField(max_length=200)
    # body       = models.TextField()
    body       = RichTextField()
    status     = models.ForeignKey(JournalStatus, on_delete=models.CASCADE, related_name='journalStatus')
    created_at = models.DateField()
    updated_at = models.DateField(auto_now=True)
    header     = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title + self.status.name
    
    def get_absolute_url(self):
        return reverse('journal:detail', kwargs={'pk' : self.pk})
    
class JournalImage(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    images  = models.ImageField(upload_to=get_image_name, blank=True, null=True)

    class Meta:
        verbose_name        = 'Images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.journal.title + self.journal.author.username
