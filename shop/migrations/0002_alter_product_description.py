# Generated by Django 4.1.6 on 2023-04-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=2050),
        ),
    ]
