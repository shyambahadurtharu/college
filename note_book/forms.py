from django import forms
from note_book.models import Level, Semester, NoteBook

class NoteForm(forms.Form):
   
    class Meta:
        model = NoteBook
        fields = ["file_upload","course_name","level_id","semester_id"]
       
            
           
 
   