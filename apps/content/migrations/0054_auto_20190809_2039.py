# Generated by Django 2.2.2 on 2019-08-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0053_auto_20190809_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='order',
            field=models.PositiveSmallIntegerField(default=100, help_text='Je höher, desto weiter oben', verbose_name='Sortierung'),
        ),
        migrations.AlterField(
            model_name='menucategory1',
            name='order',
            field=models.PositiveSmallIntegerField(default=100, help_text='Je höher, desto weiter oben.', verbose_name='Sortierung'),
        ),
    ]