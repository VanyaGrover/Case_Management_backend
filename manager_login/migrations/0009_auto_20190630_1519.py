# Generated by Django 2.2.2 on 2019-06-30 15:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager_login', '0008_auto_20190630_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.UUIDField(default=uuid.UUID('02b370c9-f8a5-4f0c-b4b0-0c496120de53'), editable=False, primary_key=True, serialize=False),
        ),
    ]
