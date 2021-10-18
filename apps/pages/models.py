from solo.models import SingletonModel
from django.db import models


class Contact(SingletonModel):
    formular_titel = models.CharField(default='Tisch reservieren', verbose_name='Formular / Titel', max_length=200)
    formular_hinweise = models.TextField(default='Hinweise: Reservierungen für den gleichen Tag sind nur bis 16 Uhr '
                                                 'online möglich, danach bitte in der Bar anrufen. Die Reservierung '
                                                 'wird erst nach der Bestätigung durch uns gültig. Bitte kontrolliert '
                                                 'Euer E-Mail Postfach. Hochtische mit Barhockern werden von uns als '
                                                 'normale Tische behandelt. Eine Reservierung ist nur entweder im '
                                                 '(Winter-)Biergarten oder in der Bar möglich.',
                                         verbose_name='Formular / Hinweise')
    formular_biergarten = models.CharField(default='Biergarten', max_length=100,
                                           verbose_name='Formular / Ort / Biergarten')
    formular_biergarten_verfuegbar = models.BooleanField(default=True,
                                                         verbose_name='Formular / Ort / Biergarten auswählbar')
    formular_bar_verfuegbar = models.BooleanField(default=True, verbose_name='Formular / Ort / Bar auswählbar')
    formular_button = models.CharField(default='Jetzt reservieren', max_length=100, verbose_name='Formular / Bar')
    formular_hinweis = models.TextField(default='Die Reservierung wird erst nach der Bestätigung durch uns gültig. '
                                                'Bitte kontrolliert Euer E-Mail Postfach.',
                                        verbose_name='Formular / Hinweis')

    def __str__(self):
        return "Kontakt"

    class Meta:
        verbose_name = "Kontakt"
