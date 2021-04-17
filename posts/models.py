from django.db import models
from account.models import Author


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    image = models.ImageField(upload_to='posts')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.author
