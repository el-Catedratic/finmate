# Generated by Django 3.0.4 on 2021-04-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_transaction_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sentiment',
            field=models.IntegerField(default=0),
        ),
    ]
