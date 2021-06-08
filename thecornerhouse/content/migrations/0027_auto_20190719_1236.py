# Generated by Django 2.2.2 on 2019-07-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_auto_20190701_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='article_section_big_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Artikel-Section große Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='article_section_small_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Artikel-Section kleine Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='events_section_big_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Events-Section große Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='events_section_small_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Events-Section kleine Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='gallery_section_big_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Galerie-Section große Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='gallery_section_small_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Galerie-Section kleine Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='hello_section_big_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Hallo-Section große Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='hello_section_small_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Hallo-Section kleine Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='hello_section_text_big',
            field=models.TextField(default='', verbose_name='Hallo-Section Fetter Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='hello_section_text_small',
            field=models.TextField(default='', verbose_name='Hallo-Section Normaler Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='menu_section_big_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Menu-Section große Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='menu_section_small_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Menu-Section kleine Überschrift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='table_reserve_button',
            field=models.CharField(default='', max_length=100, verbose_name='Zum-Kontakt-Section Button Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='table_reserve_heading',
            field=models.CharField(default='', max_length=100, verbose_name='Zum-Kontakt-Section Überschrift'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_1_heading',
            field=models.TextField(help_text='2 Zeilen empfohlen.', verbose_name='Slider-Slide-1 Überschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_1_subheading',
            field=models.CharField(max_length=100, verbose_name='Slider-Slide-1 Unterüberschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_2_heading',
            field=models.TextField(help_text='2 Zeilen empfohlen.', verbose_name='Slider-Slide-2 Überschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_2_subheading',
            field=models.CharField(max_length=100, verbose_name='Slider-Slide-2 Unterüberschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_3_heading',
            field=models.TextField(help_text='2 Zeilen empfohlen.', verbose_name='Slider-Slide-3 Überschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_3_subheading',
            field=models.CharField(max_length=100, verbose_name='Slider-Slide-3 Unterüberschrift'),
        ),
    ]
