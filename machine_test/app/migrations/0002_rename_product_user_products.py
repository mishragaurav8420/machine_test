# Generated by Django 4.1.7 on 2023-06-28 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='product',
            new_name='products',
        ),
    ]