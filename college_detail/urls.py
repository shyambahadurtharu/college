from django.urls import path
from college_detail.views import college_home, add_college, edit_college, delete_college
app_name ="college_detail"

urlpatterns = [
    path("college_home/", college_home, name="home"),
    path("add_college/", add_college, name="add_college"),
    path("edit_college/<int:college_id>/", edit_college, name="edit_college"),
    path("delete_college", delete_college, name="delete_college"),
]