# Generated by Django 4.1.2 on 2024-02-07 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='user_ip_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.useripaddress'),
        ),
    ]
