from django import forms
from college_detail.models import CollegeDetail
from django.forms import ModelForm
class CollegeDetailForm(forms.ModelForm):
    class Meta:
        model= CollegeDetail
        fields =["picture", "college_name", "address", "contact", "website", "program", "description",]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update({'class':'form-control'})
        self.fields['college_name'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        self.fields['contact'].widget.attrs.update({'class':'form-control'})
        self.fields['website'].widget.attrs.update({'class':'form-control'})
        self.fields['program'].widget.attrs.update({'class':'form-control', 'placeholder':'CSIT/BCA/BIT/BBA/'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})