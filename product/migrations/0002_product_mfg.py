# Generated by Django 4.0 on 2022-07-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mfg',
            field=models.TextField(default='non experiable'),
        ),
    ]
