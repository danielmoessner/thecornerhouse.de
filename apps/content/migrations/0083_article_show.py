# Generated by Django 4.0.2 on 2022-07-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0082_alter_job_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
