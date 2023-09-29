from django import forms
from note_book.models import Level, Semester, NoteBook

class NoteForm(forms.Form):
   
    class Meta:
        model = NoteBook
        fields = '__all__'
        widgets = { 'file_upload': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'course_name': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'level_id': forms.Select(attrs={ 'class': 'form-select' }),
            'semester': forms.Select(attrs={ 'class': 'form-select' }),
        }    
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semeter_id'].queryset = Semester.objects.none()
 
        if 'level' in self.data:
            try:
                level_id = int(self.data.get('level'))
                self.fields['level_id'].queryset = Semester.objects.filter(country_id=level_id).order_by('semester_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['semester_id'].queryset = self.instance.levle.semester_id_set.order_by('semester_name')