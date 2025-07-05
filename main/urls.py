from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('life-insurance/', views.life_insurance, name='life_insurance'),
    path('health-insurance/', views.health_insurance, name='health_insurance'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('quote/', views.quote, name='quote'),
]