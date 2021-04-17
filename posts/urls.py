from django.urls import path
from .views import home, get_post

urlpatterns = [
    path('', home, name='posts'),
    path('<int:post_id>', get_post, name='post_detail')
]
