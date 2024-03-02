from django.contrib import admin
from .models import UserProfile, Events
admin.site.register(UserProfile)
admin.site.register(Events)