# Generated by Django 4.1.3 on 2023-01-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_avatar_imagen_alter_avatar_user_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(default='/avatars/avatarpordefecto.png', upload_to='avatars'),
        ),
    ]
