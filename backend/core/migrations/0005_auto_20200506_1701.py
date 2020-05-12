# Generated by Django 3.0.5 on 2020-05-06 17:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_delete_group"),
    ]

    operations = [
        migrations.RemoveField(model_name="sheep", name="father",),
        migrations.RemoveField(model_name="sheep", name="mother",),
        migrations.CreateModel(
            name="Birth",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateTimeField()),
                ("newborns_quantity", models.IntegerField()),
                ("observations", models.TextField()),
                (
                    "sheep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="births", to="core.Sheep"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="births", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.AddField(
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