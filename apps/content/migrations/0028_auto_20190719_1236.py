# Generated by Django 2.2.2 on 2019-07-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0027_auto_20190719_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='location',
            field=models.CharField(blank=True, help_text='Im Blog klein angezeigt.', max_length=100, null=True, verbose_name='Ort'),
        ),
    ]
