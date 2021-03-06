# Generated by Django 2.2.6 on 2019-11-09 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StoryVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.PositiveSmallIntegerField()),
                ('tstamp', models.DateTimeField()),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hacker_news.Story')),
            ],
        ),
    ]
