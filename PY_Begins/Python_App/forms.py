from django import forms
from django.contrib.auth import authenticate

class login_form(forms.Form):
    username = forms.CharField(label='User Id', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        User = authenticate(username=username, password=password)

        if not User:
            raise forms.ValidationError("Incorrect username or password")

        # return super(login_form, self).clean()