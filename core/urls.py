from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products140231/',views.product,name='product'),
    path('contact140231/',views.contact,name='contact'),
    path('about140231/',views.about,name='about'),
]
