from django.contrib import admin
from note_book.models import Level, Semester, NoteBook
# Register your models here.
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "level_name")

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("id", "semester_name")
@admin.register(NoteBook)
class NoteBookAdmin(admin.ModelAdmin):
    list_display = ("id", "file_upload","course_name","level_id","semester_id")