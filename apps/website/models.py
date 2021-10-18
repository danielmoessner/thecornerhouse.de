from django.db import models


class Seo(models.Model):
    url = models.CharField(max_length=200, unique=True, blank=True, verbose_name='Url',
                           help_text='Aktiviert sich wenn diese Url in der Leiste ist. Leer für Standard oder auch '
                                     'immer aktiv.')
    title_tag = models.CharField(max_length=200, verbose_name='Titel')
    meta_description = models.TextField(verbose_name='Beschreibung')

    def __str__(self):
        if self.url:
            return '/{}: {}'.format(self.url, self.title_tag)
        return self.title_tag

    class Meta:
        verbose_name = 'SEO Einstellung'
        verbose_name_plural = 'SEO Einstellungen'


class CustomCode(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    url = models.CharField(max_length=200, blank=True, verbose_name='Url')
    LOCATIONS = [('HEAD', 'Head'), ('BODY', 'Body')]
    location = models.CharField(choices=LOCATIONS, max_length=200, verbose_name='Ort',
                                help_text='Wo soll der Code eingebunden werden?')
    code = models.TextField(verbose_name='Code', help_text='Der Code wird nicht validiert und sollte richtig sein.')

    def __str__(self):
        if self.url:
            return '/{}: {}'.format(self.url, self.name)
        return self.name

    class Meta:
        verbose_name = 'Eigener Code'
        verbose_name_plural = 'Eigener Code'


class StaticPage(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(unique=True, verbose_name='Slug',
                            help_text='Wie soll die Seite in der URL-Leiste erscheinen oder heißen?')
    shown_in_footer = models.BooleanField(verbose_name='Angezeigt im Footer',
                                          help_text='Im Footer den Link zur Seite anzeigen?')
    shown_in_navigation = models.BooleanField(verbose_name='Angezeigt in der Navigation',
                                              help_text='In der Navigation anzeigen?')
    html_activated = models.BooleanField(verbose_name='Html Code aktiviert',
                                        help_text='Soll der Inhalt als Html Code gerendert werden?')
    content = models.TextField(verbose_name='Inhalt')

    class Meta:
        verbose_name = 'Statische Seite'
        verbose_name_plural = 'Statische Seiten'

    def __str__(self):
        return str(self.name)
