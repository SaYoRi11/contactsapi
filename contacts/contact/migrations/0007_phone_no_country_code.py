# Generated by Django 3.2.7 on 2021-09-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_remove_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_no',
            name='country_code',
            field=models.CharField(default='+1', max_length=10),
        ),
    ]
