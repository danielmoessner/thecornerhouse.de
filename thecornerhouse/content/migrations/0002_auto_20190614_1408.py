# Generated by Django 2.2.2 on 2019-06-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
    ]
