# Generated by Django 5.0.1 on 2024-01-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_cafemenu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafemenu',
            name='options',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]