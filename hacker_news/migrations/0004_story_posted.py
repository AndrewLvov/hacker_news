# Generated by Django 2.2.6 on 2019-12-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0003_increase_url_max_size_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='posted',
            field=models.DateTimeField(null=True),
        ),
    ]
