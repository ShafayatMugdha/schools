# Generated by Django 2.2.3 on 2019-07-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
