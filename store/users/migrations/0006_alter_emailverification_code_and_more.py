# Generated by Django 4.0 on 2024-10-02 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_emailverification_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 12, 42, 6, 105099, tzinfo=utc)),
        ),
    ]
