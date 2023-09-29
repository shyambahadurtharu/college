from django.urls import path 
from post.views import home_feed, add_post, edit_post, delete_post, like_post, comment_post, delete_comment
app_name = "post"
urlpatterns = [
    path("feed/", home_feed, name="home"),
    path("create_post/", add_post, name="add_post"),
    path("change_post/<int:post_id>/", edit_post, name="edit_post"),
    path("remove-post/", delete_post, name="delete_post"),
    path("like_post/<int:post_id>/", like_post, name="like_post"),
    path("comment/<int:post_id>/", comment_post, name="comment_post"),
    path("delete_comment/<int:comment_id>/", delete_comment, name="delete_comment"),
]