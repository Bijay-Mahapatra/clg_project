# Generated by Django 5.1.3 on 2025-03-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin_signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
