# Generated by Django 5.1 on 2024-08-25 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_rename_discription_toys_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toys',
            new_name='Toy',
        ),
    ]
