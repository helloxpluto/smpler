# Generated by Django 3.1.4 on 2020-12-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smpler', '0002_auto_20201216_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
