# Generated by Django 3.2.5 on 2021-07-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forexapp', '0002_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]