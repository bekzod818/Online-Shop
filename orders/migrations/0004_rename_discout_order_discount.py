# Generated by Django 3.2.6 on 2021-08-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210822_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discout',
            new_name='discount',
        ),
    ]
