# Generated by Django 3.2.10 on 2021-12-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_alter_mobile_jan_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='jan_code',
            field=models.IntegerField(unique=True),
        ),
    ]
