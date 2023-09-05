# Generated by Django 4.2.3 on 2023-07-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_mail', models.CharField(max_length=50)),
                ('cust_number', models.IntegerField()),
            ],
        ),
    ]
