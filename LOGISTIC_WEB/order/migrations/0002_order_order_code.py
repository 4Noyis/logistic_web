# Generated by Django 5.0.6 on 2024-07-30 10:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(default=uuid.uuid4, max_length=20),
        ),
    ]
