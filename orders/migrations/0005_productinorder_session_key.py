# Generated by Django 3.1.3 on 2020-12-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20201224_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='session_key',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
