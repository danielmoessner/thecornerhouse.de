# Generated by Django 2.2.2 on 2019-06-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20190614_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='article/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='image',
            field=models.ImageField(upload_to='article_category/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='gallery/', verbose_name='Bild'),
        ),
    ]
