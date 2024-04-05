# Generated by Django 5.0.3 on 2024-04-04 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('snippet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='snippets.snippet')),
            ],
        ),
    ]
