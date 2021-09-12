# Generated by Django 3.0.4 on 2020-04-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probn', '0003_news2'),
    ]

    operations = [
        migrations.CreateModel(
            name='News3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('post', models.TextField()),
                ('date', models.DateTimeField()),
                ('photo', models.ImageField(height_field=100, upload_to='upload_to/pr', width_field=100)),
            ],
        ),
    ]
