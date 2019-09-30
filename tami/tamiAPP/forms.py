from django import forms
from .models import userSub

class userSubForm(forms.ModelForm):
    description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'got coffee for the office', 'class':'description rounded'}))
    where = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Amazon', 'class':'where rounded'}))

    class Meta:
        model = userSub
        fields = [
            'description',
            'where'
        ]