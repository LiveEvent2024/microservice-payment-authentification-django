# Generated by Django 4.2.8 on 2023-12-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_expirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.IntegerField(),
        ),
    ]
