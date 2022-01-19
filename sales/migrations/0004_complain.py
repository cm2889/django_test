# Generated by Django 3.1.7 on 2022-01-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
