# Generated by Django 4.1.3 on 2023-01-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatars\\avatarpordefecto.png', upload_to='profile_pics'),
        ),
    ]
