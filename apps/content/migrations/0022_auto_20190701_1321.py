# Generated by Django 2.2.2 on 2019-07-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_menucategory_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPPQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Inhalt')),
                ('unit', models.CharField(choices=[('NONE', 'Keine'), ('L', 'Liter'), ('ML', 'Milliliter'), ('CL', 'Centiliter')], default='L', max_length=20, verbose_name='Einheit')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Preis')),
            ],
            options={
                'verbose_name': 'Speisekarte Getränkepreis',
                'verbose_name_plural': 'Speisekarte Getränkepreise',
                'ordering': ['unit', 'content', 'price'],
            },
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='content',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='content1',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='price2',
        ),
        migrations.AddField(
            model_name='menuentry',
            name='ppq',
            field=models.ManyToManyField(related_name='menu_entries', to='content.MenuPPQ'),
        ),
    ]
