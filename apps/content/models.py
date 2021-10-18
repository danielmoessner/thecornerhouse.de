from image_optimizer.fields import OptimizedImageField
from django.core.exceptions import ObjectDoesNotExist
from image_optimizer.utils import image_optimizer
from django.utils import timezone
from django.db import models
from datetime import datetime


class Setting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='setting-files/', verbose_name='Datei')

    class Meta:
        verbose_name = 'Einstellung'
        verbose_name_plural = 'Einstellungen'
        ordering = ['key']

    def __str__(self):
        return str(self.key)

    @staticmethod
    def get_dict(page):
        settings = Setting.objects.filter(key__startswith=page)
        settings_dict = {}
        for setting in list(settings):
            setting_key = setting.key.replace(page + '/', '').replace('/', '_').replace('-', '')
            settings_dict[setting_key] = setting.file
        return settings_dict

    def save(self, *args, **kwargs):
        optimize = True
        if self.pk:
            setting_old = Setting.objects.get(pk=self.pk)
            if setting_old.file == self.file:
                optimize = False
        file_ending = self.file.path.split('.')[-1]
        if file_ending.lower() not in ['png', 'jpg', 'jpeg']:
            optimize = False
        if optimize:
            self.file = image_optimizer(image_data=self.file)
        super().save(*args, **kwargs)


class Member(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    title = models.CharField(max_length=200, verbose_name='Titel')
    image = models.ImageField(upload_to='members/', verbose_name='Bild')
    order = models.PositiveSmallIntegerField(default=100, verbose_name='Sortierung',
                                             help_text='Je höher, desto weiter oben.')

    class Meta:
        verbose_name = 'Teammitglied'
        verbose_name_plural = 'Teammitglieder'
        ordering = ['-order']

    def __str__(self):
        return str(self.name)


class ArticleCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(unique=True, help_text='Wie soll die Kategorie in der URL-Leiste erscheinen oder heißen?')
    image = OptimizedImageField(upload_to='article_category/', verbose_name='Bild')
    featured = models.BooleanField(verbose_name='Featured', help_text='Auf der Startseite anzeigen? Maximal 3.')

    class Meta:
        verbose_name = 'Artikel Kategorie'
        verbose_name_plural = 'Artikel Kategorien'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, verbose_name='Kategorie')
    location = models.CharField(max_length=100, verbose_name='Ort', help_text='Im Blog klein angezeigt.', blank=True,
                                null=True)
    image = OptimizedImageField(upload_to='article/', verbose_name='Bild')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Datum und Uhrzeit', default=datetime.now,
                                help_text='Beispiel Datum: 19.07.2019<br>'
                                          'Beispiel Uhrzeit: 14:49:00')
    text = models.TextField(blank=True, verbose_name='Text')
    slug = models.SlugField(unique=True, help_text='Wie soll die Kategorie in der URL-Leiste erscheinen oder heißen?')

    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        ordering = ['-date', 'title']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_day(self):
        text = ''
        if self.date:
            text = timezone.localtime(self.date).strftime('%d')
        return text

    def get_month(self):
        text = ''
        months = {'Jan': 'Januar', 'Feb': 'Februar', 'Mar': 'März', 'Apr': 'April', 'May': 'Mai', 'Jun': ' Juni',
                  'Jul': 'Juli', 'Aug': 'August', 'Sep': 'September', 'Oct': 'Oktober', 'Nov': 'November',
                  'Dec': 'Dezember'}
        if self.date:
            text = timezone.localtime(self.date).strftime('%b')
            for key, value in months.items():
                text = text.replace(str(key), value)
        return text

    def get_time(self):
        text = ''
        if self.date:
            text = timezone.localtime(self.date).strftime('%H:%M')
        return text

    def get_date(self):
        text = ''
        months = {'Jan': 'Januar', 'Feb': 'Februar', 'Mar': 'März', 'Apr': 'April', 'May': 'Mai', 'Jun': ' Juni',
                  'Jul': 'Juli', 'Aug': 'August', 'Sep': 'September', 'Oct': 'Oktober', 'Nov': 'November',
                  'Dec': 'Dezember'}
        if self.date:
            text = timezone.localtime(self.date).strftime('%d. %b %Y')
            for key, value in months.items():
                text = text.replace(str(key), value)
        return text

    def get_location(self):
        text = ''
        if self.location:
            text = self.location
        return text

    def get_long_title(self):
        text = '{} - {}'.format(self.title, self.text)
        text = '{}..'.format(text[:38])
        return text

    def get_intro(self):
        return self.text[:min(len(self.text), 140)] + '..'


class MenuCategory1(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    order = models.PositiveSmallIntegerField(default=100, verbose_name='Sortierung',
                                             help_text='Je höher, desto weiter oben.')

    class Meta:
        verbose_name = 'Speisekarte Kategorie 1'
        verbose_name_plural = 'Speisekarte Kategorien 1'
        ordering = ['-order', 'name']

    def __str__(self):
        text = '{} - {}'.format(self.order, self.name)
        return text


class MenuCategory(models.Model):
    category1 = models.ForeignKey(MenuCategory1, on_delete=models.SET_NULL, null=True, verbose_name='Kategorie 1',
                                  related_name='categories')
    name = models.CharField(max_length=200, verbose_name='Name')
    featured_on_index = models.BooleanField(default=False, verbose_name='Auf der Startseite angezeigt')
    order = models.PositiveSmallIntegerField(default=100, verbose_name='Sortierung',
                                             help_text='Je höher, desto weiter oben')
    image = models.ImageField(upload_to='menu_category/', blank=True, null=True, verbose_name='Bild')

    class Meta:
        verbose_name = 'Speisekarte Kategorie 2'
        verbose_name_plural = 'Speisekarte Kategorien 2'
        ordering = ['-order', 'name']

    def __str__(self):
        text = '{} - {}'.format(self.order, self.name)
        return text


class MenuPPQ(models.Model):
    UNITS = (('NONE', 'Keine'), ('L', 'Liter'), ('ML', 'Milliliter'), ('CL', 'Centiliter'))
    content = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Inhalt', default=1)
    unit = models.CharField(choices=UNITS, max_length=20, default='NONE', verbose_name='Einheit')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preis', default=0)

    class Meta:
        verbose_name = 'Speisekarte Preise'
        verbose_name_plural = 'Speisekarte Preise'
        ordering = ['unit', 'content', 'price']

    def __str__(self):
        if self.unit == 'NONE':
            text = '{}€'.format(self.price)
        else:
            text = '{}{} {}€'.format(self.content, str(self.unit).lower(), self.price)
        return text


class MenuAdditive(models.Model):
    number = models.PositiveSmallIntegerField(unique=True, verbose_name='Nummer')
    description = models.CharField(max_length=200, verbose_name='Beschreibung')

    class Meta:
        verbose_name = 'Speisekarte Zusatzstoff'
        verbose_name_plural = 'Speisekarte Zusatzstoffe'
        ordering = ['number']

    def __str__(self):
        text = '{} {}'.format(self.number, self.description)
        return text


class MenuEntry(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, verbose_name='Kategorie',
                                 related_name='menu_entries')
    description = models.TextField(blank=True, verbose_name='Beschreibung')
    ppqs = models.ManyToManyField(MenuPPQ, related_name='menu_entries', blank=True)
    additives = models.ManyToManyField(MenuAdditive, related_name='menu_entries', blank=True)

    class Meta:
        verbose_name = 'Speisekarte Eintrag'
        verbose_name_plural = 'Speisekarte Einträge'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Bild')
    featured_on_index = models.BooleanField(verbose_name='Featured auf der Startseite',
                                            help_text='Auf der Startseite in der Gallerie anzeigen? Maximal 5.')
    featured_on_about = models.BooleanField(verbose_name='Featured auf der Über uns Seite',
                                            help_text='Auf der Über uns Seite in der Gallerie anzeigen? Maximal 5.')

    class Meta:
        verbose_name = 'Galerie Bild'
        verbose_name_plural = 'Galerie Bilder'

    def __str__(self):
        if self.featured_on_about and self.featured_on_index:
            text = 'Startseite - Über uns - {}'.format(self.image)
        elif self.featured_on_about:
            text = 'Über uns - {}'.format(self.image)
        elif self.featured_on_index:
            text = 'Startseite - {}'.format(self.image)
        else:
            text = '{}'.format(self.image)
        return text


class TextSnippet(models.Model):
    key = models.CharField(unique=True, max_length=60)
    text = models.TextField(blank=True)
    notes = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        verbose_name = 'Textbaustein'
        verbose_name_plural = 'Textbausteine'
        ordering = ['key']

    def __str__(self):
        return '{}-{}'.format(self.get_key_in_beautiful_format(), self.text[:40])

    # getters
    def get_key_in_beautiful_format(self):
        key_length = len(self.key)
        spacer = '-' * (60 - key_length)
        return '{}{}'.format(self.key, spacer)

    @staticmethod
    def get_dict(page=''):
        snippets = TextSnippet.objects.filter(key__startswith=page)
        snippets_dict = {}
        for snippet in list(snippets):
            snippet_key = snippet.key.replace(page + '/', '').replace('/', '_').replace('-', '')
            snippets_dict[snippet_key] = snippet.text
        return snippets_dict

    @staticmethod
    def get(key):
        try:
            snippet = TextSnippet.objects.get(key=key)
            snippet = snippet.text
        except ObjectDoesNotExist:
            snippet = ''
        return snippet
