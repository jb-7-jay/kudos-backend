from celery import shared_task
from django.utils import timezone
from .models import KudosQuota
from .constants import DEFAULT_KUDOS_QUOTA


@shared_task
def reset_kudos_quotas():
    KudosQuota.objects.update(
        kudos_remaining=DEFAULT_KUDOS_QUOTA,
        updated_at=timezone.now(),
    )
    print(f"Kudos reset at {timezone.now()}")
