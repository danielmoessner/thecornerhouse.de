# Generated by Django 4.0.2 on 2022-02-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_jobs_thanks_pre_jobs_thanks_text_jobs_thanks_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='formular_button',
            field=models.CharField(default='Jetzt reservieren', max_length=100, verbose_name='Formular / Button'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='thanks_text',
            field=models.TextField(default='Wir werden uns schnellstmöglich bei Ihnen melden.', verbose_name='Danke / Text'),
        ),
    ]
