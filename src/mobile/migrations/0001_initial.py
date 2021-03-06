# Generated by Django 3.2.10 on 2021-12-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('model', models.TextField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('jan_code', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('status', models.IntegerField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
