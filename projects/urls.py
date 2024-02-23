from django.urls import path
from . import views
urlpatterns=[
  path('landing/', views.landing, name="landing"),
  path('login/', views.loginpage, name="login"),
  path('register/', views.registerpage, name="register") ,
  path('services/', views.services, name="services") ,
  path('logout/', views.logoutpage, name='logout'),
  path('medical_services/', views.med_ser, name='med_ser'),
  path('wellness/', views.wellness, name='wellness'),
  path('user_profile/', views.user_profile, name='user_profile'),
  path('home/', views.home, name='home'),
  path('vac_base/', views.vaccination_base, name='vac_base'),
  path('diet_cons1/', views.diet_cons1, name='diet_cons1'),
  path('diet_cons2/', views.diet_cons2, name='diet_cons2'),
  path('vac_base_archive/', views.vac_base_archive, name='vac_base_archive'),
]
