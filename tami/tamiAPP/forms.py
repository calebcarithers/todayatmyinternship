from django import forms
from .models import userSub

class userSubForm(forms.ModelForm):
    description = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'what', 'class':'description'}))
    where = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'where', 'class':'where'}))

    class Meta:
        model = userSub
        fields = [
            'description',
            'where'
        ]