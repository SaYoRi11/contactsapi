# Generated by Django 3.2.7 on 2021-09-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210920_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_no',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]