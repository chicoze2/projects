# Generated by Django 4.2.4 on 2023-08-05 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0002_protocolo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protocolo',
            old_name='user',
            new_name='author',
        ),
    ]
