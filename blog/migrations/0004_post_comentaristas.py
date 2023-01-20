# Generated by Django 4.1.3 on 2023-01-16 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comentaristas',
            field=models.ManyToManyField(blank=True, related_name='comentaristas', to=settings.AUTH_USER_MODEL),
        ),
    ]
