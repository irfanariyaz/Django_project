# Generated by Django 4.0.2 on 2023-06-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_classifields_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifields',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
