# Generated by Django 3.0.5 on 2020-05-06 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20200506_1701"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sheep",
            name="birth",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="broods",
                to="core.Birth",
            ),
        ),
    ]
