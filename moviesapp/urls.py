from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('home', index, name="index"),
    path('movies', movies, name="movies"),
    path('search', search, name="seach"),
    path('registeruser', registeruser, name="registeruser"),
    path('verifyuser', verifyuser, name="verifyuser"),
    path('logout', logout, name="logout"),
]
