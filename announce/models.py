from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

def get_image_name(instance, filename):
    image_name = instance.announce.name
    return "images/{}/{}".format(image_name, filename)

def get_file_name(instance, filename):
    file_name = instance.announce.name
    return "files/{}/{}".format(file_name, filename)

class AnnounceType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class AnnounceStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Announce(models.Model):
    ''' for announce create '''
    is_type = models.ForeignKey(AnnounceType, on_delete=models.CASCADE, related_name='announce_type')
    status = models.ForeignKey(AnnounceStatus, on_delete=models.CASCADE, related_name='announce_status')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    # detail = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    reads = models.ManyToManyField(User, related_name='readers')
    
    def __str__(self):
        return '(' + self.is_type + ')' + self.name + '(' + self.author.username + ')' + self.created_at.strftime('%a, %d %b %Y %H:%M:%S') + '--' + str(self.number_of_reader()) + ' reader'

    def number_of_reader(self):
        return self.reads.count()
    
class AnnounceImage(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=get_image_name, blank=True, null=True)
    
    def __str__(self):
        return self.announce.name + '(' + self.announce.author.username + ')'
    
class AnnounceFile(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    files = models.FileField(upload_to=get_file_name, blank=True, null=True)
    
    def __str__(self):
        return self.announce.name + '(' + self.announce.author.username + ')'
    
class Comment(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return 'Comment by ' + self.author.username + ' on ' + self.created_at.strftime('%a, %d %b %Y %H:%M')
    