# Generated by Django 3.2 on 2021-04-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_merge_0009_auto_20210414_2121_0010_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='credit_score',
            field=models.FloatField(default=0.0),
        ),
    ]
