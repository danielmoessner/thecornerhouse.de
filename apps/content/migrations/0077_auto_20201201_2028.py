# Generated by Django 2.2.16 on 2020-12-01 19:28

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0076_auto_20201126_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='article/', verbose_name='Bild'),
        ),
    ]
