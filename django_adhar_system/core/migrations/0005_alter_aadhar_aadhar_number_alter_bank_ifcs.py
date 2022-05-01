# Generated by Django 4.0.4 on 2022-05-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_aadhar_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar',
            name='aadhar_number',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bank',
            name='ifcs',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]