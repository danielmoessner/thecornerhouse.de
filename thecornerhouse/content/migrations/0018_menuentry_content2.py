# Generated by Django 2.2.2 on 2019-07-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20190624_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuentry',
            name='content2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Inhalt 2'),
        ),
    ]
