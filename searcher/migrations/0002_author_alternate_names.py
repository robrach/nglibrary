# Generated by Django 4.1 on 2022-09-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='alternate_names',
            field=models.TextField(default='hej'),
            preserve_default=False,
        ),
    ]