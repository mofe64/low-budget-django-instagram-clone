from django.urls import path
from .views import home, get_post, get_post_create

urlpatterns = [
    path('', home, name='posts'),
    path('<int:post_id>', get_post, name='post_detail'),
    path('new', get_post_create, name='create_post')
]
