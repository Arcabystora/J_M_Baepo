# Generated by Django 5.0.1 on 2024-02-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_cafeoption_option_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlist',
            old_name='order_option',
            new_name='order_menu',
        ),
        migrations.RemoveField(
            model_name='orderlist',
            name='order_price',
        ),
        migrations.RemoveField(
            model_name='orderlist',
            name='order_quantity',
        ),
        migrations.AddField(
            model_name='orderlist',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='order_status',
            field=models.CharField(choices=[('pending', '대기'), ('processing', '진행중'), ('completed', '완료됨')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='total_quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True),
        ),
    ]
