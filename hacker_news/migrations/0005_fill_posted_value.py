# Generated by Django 2.2.6 on 2019-12-17 08:33

from datetime import datetime as dtime
import pytz
import requests

from django.db import migrations
from project import API_URL


def fill_posted_time(apps, schema_editor):
    Story = apps.get_model("hacker_news", "Story")
    for story in Story.objects.all():
        response = requests.get(f"{API_URL}/v0/item/{story.id}.json?print=pretty")
        if response.status_code != 200:
            print(f"Hacker News returned HTTP {response.status_code}")

        story_info = response.json()
        print(f"Adding posted value {story_info['time']} for {story.title[:50]}")
        story.posted = pytz.utc.localize(
            dtime.utcfromtimestamp(
                story_info['time']))
        story.save()


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0004_story_posted'),
    ]

    operations = [
        migrations.RunPython(fill_posted_time, migrations.RunPython.noop),
    ]
