# Generated by Django 4.1.3 on 2022-11-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_customuser_tiger_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='animals',
            field=models.ManyToManyField(blank=True, to='restapi.animal'),
        ),
    ]
