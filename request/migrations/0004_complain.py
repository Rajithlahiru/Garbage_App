# Generated by Django 3.2.5 on 2022-08-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_rename_username_request_user_request_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('detail', models.TextField()),
            ],
        ),
    ]
