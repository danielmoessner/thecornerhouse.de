# Generated by Django 2.2.2 on 2019-06-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20190624_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='featured_on_index',
            field=models.BooleanField(default=False, verbose_name='Auf der Startseite angezeigt'),
        ),
    ]
