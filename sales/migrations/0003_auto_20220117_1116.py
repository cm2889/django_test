# Generated by Django 3.1.7 on 2022-01-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
