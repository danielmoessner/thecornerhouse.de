# Generated by Django 2.2.16 on 2020-12-01 19:34

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0077_auto_20201201_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='article/', verbose_name='Bild1'),
        ),
    ]