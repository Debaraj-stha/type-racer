# Generated by Django 5.0.7 on 2024-07-31 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quote',
            new_name='Text',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='quote',
            new_name='text',
        ),
    ]