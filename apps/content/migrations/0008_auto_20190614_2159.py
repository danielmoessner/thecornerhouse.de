# Generated by Django 2.2.2 on 2019-06-14 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20190614_2137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Artikel', 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': 'Artikel Kategorie', 'verbose_name_plural': 'Artikel Kategorien'},
        ),
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'verbose_name': 'Gallerie Bild', 'verbose_name_plural': 'Gallerie Bilder'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Ort', 'verbose_name_plural': 'Orte'},
        ),
        migrations.AlterModelOptions(
            name='menucategory',
            options={'verbose_name': 'Speisekarte Kategorie', 'verbose_name_plural': 'Speisekarte Kategorien'},
        ),
        migrations.AlterModelOptions(
            name='menuentry',
            options={'verbose_name': 'Speisekarte Eintrag', 'verbose_name_plural': 'Speisekarte Einträge'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.ArticleCategory', verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(blank=True, help_text='Kann leer bleiben. Uhrzeit kann weggelassen werden.', null=True, verbose_name='Datum und Uhrzeit'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media/article/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='article',
            name='location',
            field=models.CharField(help_text='Im Blog klein angezeigt.', max_length=100, verbose_name='Ort'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='Wie soll die Kategorie in der URL-Leiste erscheinen oder heißen?', unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='featured',
            field=models.BooleanField(help_text='Auf der Startseite anzeigen? Maximal 3.', verbose_name='Featured'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='image',
            field=models.ImageField(upload_to='media/article_category/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='slug',
            field=models.SlugField(help_text='Wie soll die Kategorie in der URL-Leiste erscheinen oder heißen?', unique=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='featured_on_about',
            field=models.BooleanField(help_text='Auf der Über uns Seite in der Gallerie anzeigen? Maximal 6.', verbose_name='Featured auf der Über uns Seite'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='featured_on_index',
            field=models.BooleanField(help_text='Auf der Startseite in der Gallerie anzeigen? Maximal 6.', verbose_name='Featured auf der Startseite'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='media/gallery/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='location',
            name='about_text',
            field=models.TextField(verbose_name='Über uns Text'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.TextField(verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='location',
            name='contact_mail',
            field=models.CharField(max_length=50, verbose_name='Kontakt E-Mail'),
        ),
        migrations.AlterField(
            model_name='location',
            name='contact_phone',
            field=models.CharField(max_length=50, verbose_name='Kontakt Telefon'),
        ),
        migrations.AlterField(
            model_name='location',
            name='opening_hours',
            field=models.TextField(verbose_name='Öffnungszeiten'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='menuentry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.MenuCategory', verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='menuentry',
            name='content',
            field=models.IntegerField(blank=True, help_text='Kann leer bleiben.', null=True, verbose_name='Inhalt in ml'),
        ),
        migrations.AlterField(
            model_name='menuentry',
            name='description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='menuentry',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='menuentry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preis'),
        ),
    ]
