# Generated by Django 4.1 on 2022-09-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0002_author_alternate_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='alternate_names',
            field=models.TextField(default=''),
        ),
    ]