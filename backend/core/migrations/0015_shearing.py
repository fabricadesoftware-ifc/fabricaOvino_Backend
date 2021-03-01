# Generated by Django 3.0.5 on 2020-12-10 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_delete_shearing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shearing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amountOfWool', models.FloatField()),
                ('sheep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shearing', to='core.Sheep')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shearing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]