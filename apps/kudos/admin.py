from django.contrib import admin
from .models import KudosQuota, Kudos


@admin.register(KudosQuota)
class KudosQuotaAdmin(admin.ModelAdmin):
    list_display = ("user", "kudos_remaining", "created_at", "updated_at")
    search_fields = ("user__username", "user__first_name", "user__last_name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Kudos)
class KudosAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "message", "created_at")
    search_fields = ("sender__username", "receiver__username")
    readonly_fields = ("created_at", "updated_at")
