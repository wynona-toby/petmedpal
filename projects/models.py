from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    pet_name = models.CharField(max_length=255)
    pet_breed = models.CharField(max_length=255)
    documents = models.FileField(upload_to='user_documents/', null=True, blank=True)
