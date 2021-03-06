# Generated by Django 4.0.2 on 2022-02-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0080_alter_article_id_alter_articlecategory_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titel')),
                ('date', models.DateField(verbose_name='Datum')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='category1',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='additives',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menuentry',
            name='ppqs',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='Wie soll der Artikel in der URL-Leiste erscheinen oder heißen?', unique=True),
        ),
        migrations.DeleteModel(
            name='MenuAdditive',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
        migrations.DeleteModel(
            name='MenuCategory1',
        ),
        migrations.DeleteModel(
            name='MenuEntry',
        ),
        migrations.DeleteModel(
            name='MenuPPQ',
        ),
    ]
