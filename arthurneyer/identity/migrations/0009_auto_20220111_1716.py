# Generated by Django 3.2 on 2022-01-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0008_auto_20211110_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramportfolio',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='muggumportfolio',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workportfolio',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
