# Generated by Django 3.2.5 on 2022-07-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('garbage_type', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
            ],
        ),
    ]
