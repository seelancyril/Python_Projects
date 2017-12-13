from django import forms

class bookSearch(forms.Form):
    book = forms.CharField(label='Search by Name', max_length=20)