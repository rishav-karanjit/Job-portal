# Generated by Django 3.0.2 on 2020-03-08 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0002_remove_user_connections'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='connections',
            field=models.ManyToManyField(related_name='_user_connections_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
