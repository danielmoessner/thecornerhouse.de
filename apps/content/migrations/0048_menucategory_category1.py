# Generated by Django 2.2.2 on 2019-08-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0047_menucategory1'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='category1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='content.MenuCategory1'),
        ),
    ]