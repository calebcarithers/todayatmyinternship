from django import forms
from .models import userSub

class userSubForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'what did you do @ your internship today...'}))
    where = forms.CharField()

    class Meta:
        model = userSub
        fields = [
            'description',
            'where'
        ]