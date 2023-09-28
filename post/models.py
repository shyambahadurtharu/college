from django.db import models
from django.conf import settings
# Create your models here.
class PostStatus(models.TextChoices):
    PUBLIC = ("public", "Public")
    PRIVATE = ("private", "Private")

class Post(models.Model):
    picture =models.ImageField(upload_to="posts/", blank=True, null=True)
    caption = models.CharField(max_length=100, blank=True, null=True )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.CharField(
        max_length=100,
        choices=PostStatus.choices,
        default=PostStatus.PRIVATE
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    def __str__(self):
        return str(self.id)
    @property
    def like_count(self):
        return self.like_set.filter(is_liked=True).count()
    @property
    def comment_count(self):
        return self.comment_set.count()
    
class Like(models.Model):
    is_liked = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   

    def __str__(self):
        return str(self.id)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )

class Comment(models.Model):
    text = models.CharField(max_length=150)
    comment_image=models.ImageField(upload_to="commentimage/",max_length=250, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )