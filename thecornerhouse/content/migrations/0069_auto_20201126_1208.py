# Generated by Django 2.2.16 on 2020-11-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0068_auto_20201126_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textsnippet',
            name='key',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
