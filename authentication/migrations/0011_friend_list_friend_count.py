# Generated by Django 3.2 on 2021-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_bill_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend_list',
            name='friend_count',
            field=models.IntegerField(default=0),
        ),
    ]
