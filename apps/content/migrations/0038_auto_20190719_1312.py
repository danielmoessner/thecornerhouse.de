# Generated by Django 2.2.2 on 2019-07-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0037_auto_20190719_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='menu_page_bottom_section_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Menü-Seite Untere-Section Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='menu_page_bottom_section_subheading',
            field=models.CharField(default='', max_length=100, verbose_name='Menü-Seite Untere-Section Unterüberschrift'),
            preserve_default=False,
        ),
    ]