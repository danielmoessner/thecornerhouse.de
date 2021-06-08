from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    persons = forms.IntegerField()
    time = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    location = forms.CharField(required=False)
