# Generated by Django 3.2.5 on 2022-07-14 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0001_initial'),
        ('vehicle_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_register.user'),
        ),
    ]
