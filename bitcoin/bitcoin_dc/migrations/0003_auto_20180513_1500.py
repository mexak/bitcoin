# Generated by Django 2.0.5 on 2018-05-13 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin_dc', '0002_auto_20180513_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='address_id',
            new_name='address',
        ),
    ]
