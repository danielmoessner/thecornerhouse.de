# Generated by Django 2.2.16 on 2020-09-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0065_textsnippet_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textsnippet',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]