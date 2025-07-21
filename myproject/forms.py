
from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    """
    A ModelForm for the Entry model, automatically generating fields
    based on the model definition.
    """
    class Meta:
        model = Entry
        fields = ['title', 'content'] # Specify which fields from the Entry model to include in the form
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter title here'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'placeholder': 'Write your entry content here...'}),
        }
        labels = {
            'title': 'Entry Title',
            'content': 'Entry Content',
        }