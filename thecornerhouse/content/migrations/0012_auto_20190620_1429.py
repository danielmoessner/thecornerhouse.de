# Generated by Django 2.2.2 on 2019-06-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20190620_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='slider_slide_1_heading',
            field=models.TextField(help_text='Müssen genau 2 Zeilen seien.', verbose_name='Slider Slide 1 Überschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_2_heading',
            field=models.TextField(help_text='Müssen genau 2 Zeilen seien.', verbose_name='Slider Slide 2 Überschrift'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slider_slide_3_heading',
            field=models.TextField(help_text='Müssen genau 2 Zeilen seien.', verbose_name='Slider Slide 3 Überschrift'),
        ),
    ]
