# Generated by Django 4.0.2 on 2022-02-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.TextField(max_length=256),
        ),
    ]