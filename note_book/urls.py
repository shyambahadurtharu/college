from django.urls import path 
from note_book.views import add_note, get_semester
app_name = "note_book"
urlpatterns = [
    path("get_semester/", get_semester, name="get_semester"),
    path("add_note/", add_note, name="add_note"),
]