#Portbuilder urls.py
from django.urls import path, include

from .views import StartPageView, Bio_Create, Socials_Create, ProfileView

urlpatterns = [
    path('', StartPageView.as_view(), name='index'),
    path('create/bio', Bio_Create.as_view(), name='create_bio'),
    path('create/socials', Socials_Create.as_view(), name='create_socials'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]