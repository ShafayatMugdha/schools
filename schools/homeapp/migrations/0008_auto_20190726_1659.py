# Generated by Django 2.2.3 on 2019-07-26 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_auto_20190726_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.Registration'),
        ),
    ]
