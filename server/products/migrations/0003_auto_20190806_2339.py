# Generated by Django 2.2.4 on 2019-08-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_topshops'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topshops',
            old_name='shop_tags',
            new_name='shop_card_tags',
        ),
    ]
