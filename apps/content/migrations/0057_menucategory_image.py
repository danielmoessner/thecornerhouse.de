# Generated by Django 2.2.2 on 2019-08-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0056_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category-images/', verbose_name='Bild'),
        ),
    ]
