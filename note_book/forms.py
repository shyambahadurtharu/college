from django import forms
from note_book.models import Level, Semester, NoteBook

class NoteForm(forms.Form):
    level = forms.ModelChoiceField(queryset=Level.objects.all())
    semester= forms.ModelChoiceField(queryset=Semester.objects.none())
    class Meta:
        model = NoteBook
        fields = ["file_upload", "course_name","level","semester" ]