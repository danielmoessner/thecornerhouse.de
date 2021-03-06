# Generated by Django 2.2.2 on 2019-07-25 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0044_auto_20190725_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date', 'title'], 'verbose_name': 'Artikel', 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Artikel Kategorie', 'verbose_name_plural': 'Artikel Kategorien'},
        ),
        migrations.AlterModelOptions(
            name='menuentry',
            options={'ordering': ['name'], 'verbose_name': 'Speisekarte Eintrag', 'verbose_name_plural': 'Speisekarte Einträge'},
        ),
    ]
