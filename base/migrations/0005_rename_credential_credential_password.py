# Generated by Django 5.0.6 on 2024-06-07 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_task_description_alter_task_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credential',
            old_name='credential',
            new_name='password',
        ),
    ]
