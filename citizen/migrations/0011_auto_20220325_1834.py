# Generated by Django 3.1.6 on 2022-03-25 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0010_auto_20220323_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='center',
            field=models.ForeignKey(blank=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='citizen.diagnosis_center'),
        ),
    ]