from django import forms
from post.models import Post, Comment
from django.forms import ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["picture", "caption","status", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update({'class':'form-control',})
        self.fields['caption'].widget.attrs.update({'class':'form-control','placeholder':'Please Enter your Caption'})
        self.fields['status'].widget.attrs.update({'class':'form-control'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text","comment_image",]
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"