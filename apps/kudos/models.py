from django.db import models
from django.contrib.auth.models import User
from apps.kudos.constants import DEFAULT_KUDOS_QUOTA


class KudosQuota(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="kudos_quota"
    )
    kudos_remaining = models.PositiveIntegerField(default=DEFAULT_KUDOS_QUOTA)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Kudos Remaining: {self.kudos_remaining}"


class Kudos(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="kudos_sent"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="kudos_received"
    )
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.username} - {self.receiver.username}"
