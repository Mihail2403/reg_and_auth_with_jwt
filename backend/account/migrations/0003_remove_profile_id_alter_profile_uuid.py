# Generated by Django 4.2.4 on 2023-08-23 07:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_profil_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]