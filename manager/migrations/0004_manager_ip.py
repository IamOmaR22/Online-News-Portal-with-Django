# Generated by Django 3.0.3 on 2020-03-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200227_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.TextField(default=''),
        ),
    ]