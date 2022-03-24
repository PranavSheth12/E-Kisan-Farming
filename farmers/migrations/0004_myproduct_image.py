# Generated by Django 4.0.2 on 2022-03-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_rename_area_myproduct_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproduct',
            name='image',
            field=models.FileField(default=1, help_text='Image should be in jpeg/jpg/png form and image size should be 250*250', upload_to='products'),
            preserve_default=False,
        ),
    ]
