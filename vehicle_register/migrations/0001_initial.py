# Generated by Django 3.2.5 on 2022-07-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_no', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=100)),
            ],
        ),
    ]
