# Generated by Django 3.1.7 on 2021-09-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_sheep_lots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shearing',
            name='date',
            field=models.DateField(),
        ),
    ]
