# Generated by Django 2.2.2 on 2019-06-15 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190615_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customcode',
            old_name='slug',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='seo',
            old_name='slug',
            new_name='url',
        ),
    ]
