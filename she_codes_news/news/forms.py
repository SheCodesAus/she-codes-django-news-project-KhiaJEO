from django import forms
from django.forms import ModelForm
from.models import NewsStory

class StoryForm(forms.ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        # widgets = {
        # 'pub_date': forms.DateInput(format=('%m/%d/%y'), attrs={'class':'form-control', 'placeholder':'select a date', 'type':'date'}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")
        