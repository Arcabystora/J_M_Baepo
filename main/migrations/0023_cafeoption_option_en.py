# Generated by Django 5.0.1 on 2024-02-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_cafemenu_deg_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeoption',
            name='option_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
