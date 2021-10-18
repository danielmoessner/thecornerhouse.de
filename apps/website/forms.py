from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    persons = forms.IntegerField(required=False)
    date = forms.CharField(required=False)
    time = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    location = forms.CharField(required=False)
    comment = forms.CharField(required=False)
