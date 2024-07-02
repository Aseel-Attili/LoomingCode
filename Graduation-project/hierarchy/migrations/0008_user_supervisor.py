# Generated by Django 5.0.4 on 2024-04-14 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0007_remove_user_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
