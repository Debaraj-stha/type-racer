# Generated by Django 5.0.7 on 2024-07-31 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_quote_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='data',
            new_name='text',
        ),
    ]