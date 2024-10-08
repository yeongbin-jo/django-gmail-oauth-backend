# Generated by Django 5.1.1 on 2024-09-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('key', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('value', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gmail OAuth Refresh Token',
                'verbose_name_plural': 'Gmail OAuth Refresh Tokens',
            },
        ),
    ]
