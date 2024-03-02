from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',default=None, null=True)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    age = models.IntegerField()    
    date_of_birth = models.DateField()
    email = models.CharField(max_length=255,default=None, null=True)
    address = models.TextField()
    pet_name = models.CharField(max_length=255)
    pet_breed = models.CharField(max_length=255)
    documents = models.FileField(upload_to='user_documents/', null=True, blank=True)
    def __str__(self):
        return self.name


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True)
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    def __str__(self):
        return self.title
