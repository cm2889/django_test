# Generated by Django 3.1.7 on 2022-01-17 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20220117_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]
