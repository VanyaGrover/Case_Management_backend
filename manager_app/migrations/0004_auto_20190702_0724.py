# Generated by Django 2.2.2 on 2019-07-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0003_auto_20190702_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='end_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='starting_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
