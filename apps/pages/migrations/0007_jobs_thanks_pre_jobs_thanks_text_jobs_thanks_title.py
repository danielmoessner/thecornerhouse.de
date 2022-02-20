# Generated by Django 4.0.2 on 2022-02-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_jobs_form_button_jobs_form_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='thanks_pre',
            field=models.CharField(default='Ihre Anfrage ist bei uns eingegangen', max_length=200, verbose_name='Danke / Vortitel'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='thanks_text',
            field=models.TextField(default='Wir melden uns schnellstmöglich bei Ihnen', verbose_name='Danke / Text'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='thanks_title',
            field=models.CharField(default='Vielen Dank', max_length=200, verbose_name='Danke / Titel'),
        ),
    ]