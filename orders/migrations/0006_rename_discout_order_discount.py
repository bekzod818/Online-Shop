# Generated by Django 3.2.6 on 2021-08-22 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_discount_order_discout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discout',
            new_name='discount',
        ),
    ]
