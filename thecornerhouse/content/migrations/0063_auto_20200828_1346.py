# Generated by Django 2.2.2 on 2020-08-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0062_auto_20200828_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textsnippet',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
