# Generated by Django 4.2.3 on 2023-08-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_customer_cust_mail_alter_customer_cust_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_mail',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_number',
            field=models.CharField(max_length=10),
        ),
    ]
