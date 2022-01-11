from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about),
    path('services.html', views.services),
    path('contact.html', views.contact),
]
