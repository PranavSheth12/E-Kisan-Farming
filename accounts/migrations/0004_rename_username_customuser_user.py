# Generated by Django 4.0.2 on 2022-03-14 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='username',
            new_name='User',
        ),
    ]
