from celery import shared_task
from .models import Story
from django.utils import timezone


@shared_task
def check_story_expiration():
    active_stories = Story.objects.filter(expires_at__lte=timezone.now(), expired=False)

    for story in active_stories:
        if story.expires_at <= timezone.now():
            story.expired = True
            story.save()

    return f"Checked {len(active_stories)} stories for expiration."