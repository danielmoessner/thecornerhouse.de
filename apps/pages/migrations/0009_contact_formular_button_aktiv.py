# Generated by Django 4.0.2 on 2022-05-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_contact_formular_button_alter_jobs_thanks_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='formular_button_aktiv',
            field=models.BooleanField(default=True, verbose_name='Formular / Button / Aktiv'),
        ),
    ]
