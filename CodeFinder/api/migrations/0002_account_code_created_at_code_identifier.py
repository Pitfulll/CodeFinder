# Generated by Django 5.0 on 2023-12-29 23:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('identifier', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='code',
            name='identifier',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]
