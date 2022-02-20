from apps.content.models import Job
from apps.pages.models import Contact
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Auf den Namen', widget=forms.TextInput(attrs={'placeholder': 'Muster'}))
    email = forms.CharField(label='E-Mail zur Bestätigung',
                            widget=forms.EmailInput(attrs={'placeholder': 'beispiel@email.de'}))
    phone = forms.CharField(label='Telefonnummer',
                            widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '1234 12345678'}))
    persons = forms.IntegerField(label='Anzahl an Personen',
                                 widget=forms.NumberInput(attrs={'placeholder': '1, 2, 3, 4, ..'}))
    datetime = forms.SplitDateTimeField(label='Wann ist es am besten?', widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    location = forms.ChoiceField(label='Wo ist es am besten?')
    comment = forms.CharField(label='Kommentar (optional)', widget=forms.Textarea(attrs={'rows': 1}),
                              required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        page = Contact.get_solo()
        choices = (
            ('', '---'),
        )
        if page.formular_biergarten_verfuegbar:
            choices = (*choices, (page.formular_biergarten, page.formular_biergarten))
        if page.formular_bar_verfuegbar:
            choices = (*choices, ('Bar', 'Bar'))
        self.fields['location'].choices = choices


    def clean_datetime(self):
        datetime = self.cleaned_data['datetime']
        datetime = datetime.strftime('%d.%m.%Y %H:%M')
        return datetime


class JobForm(forms.Form):
    # job = forms.ModelChoiceField(label='Job', queryset=Job.objects.all(), required=False)
    job = forms.CharField(label='Job')
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefonnummer')
    content = forms.CharField(label='Erzähl uns doch bitte 2-3 Sätze über dich', widget=forms.Textarea)
