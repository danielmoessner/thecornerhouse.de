from apps.content.models import Job
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


class JobForm(forms.Form):
    job = forms.ModelChoiceField(label='Job', queryset=Job.objects.all())
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefonnummer')
    content = forms.CharField(label='Erzähl uns doch bitte 2-3 Sätze über dich', widget=forms.Textarea)
