# Generated by Django 5.0.4 on 2024-06-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_alter_cartdb_quantity_alter_cartdb_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdb',
            name='Total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]