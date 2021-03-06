# Generated by Django 2.2.16 on 2020-12-01 20:38

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0078_auto_20201201_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='article/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='article_category/', verbose_name='Bild'),
        ),
    ]
