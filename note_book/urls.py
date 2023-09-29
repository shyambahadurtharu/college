from django.urls import path 
from note_book.views import home, add_note, get_semester
app_name = "note_book"
urlpatterns = [
    path("note_home/", home, name="note_home"),
    path("add_note/", add_note, name="add_note"),
    path("get_semester/", get_semester, name="get_semester"),
]