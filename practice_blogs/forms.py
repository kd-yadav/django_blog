from django import forms
from .models import Title, Text

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title']
        labels = {'title': ''}

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}