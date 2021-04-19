from django.urls import path

from .views import create_user

urlpatterns = [
    path('new', create_user, name='create_user')
]
