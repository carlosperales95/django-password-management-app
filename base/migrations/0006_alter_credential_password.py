# Generated by Django 5.0.6 on 2024-06-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_credential_credential_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(max_length=90),
        ),
    ]
