# Generated by Django 4.0.2 on 2023-06-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_rename_classifieds_classifields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifields',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]