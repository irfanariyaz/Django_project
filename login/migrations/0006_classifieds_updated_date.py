# Generated by Django 4.0.2 on 2023-06-24 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_classifieds_seller_delete_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifieds',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
