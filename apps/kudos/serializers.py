from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Kudos


class KudosCreateSerializer(serializers.ModelSerializer):
    receiver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="receiver"
    )
    message = serializers.CharField(allow_blank=True)

    class Meta:
        model = Kudos
        fields = ["receiver_id", "message"]

    def validate(self, data):
        sender = self.context["request"].user
        receiver = data["receiver"]

        if sender == receiver:
            raise serializers.ValidationError("You cannot send kudos to yourself.")

        if (
            not hasattr(sender, "kudos_quota")
            or sender.kudos_quota.kudos_remaining <= 0
        ):
            raise serializers.ValidationError("You have no kudos remaining to give.")

        return data

    def create(self, validated_data):
        sender = self.context["request"].user
        receiver = validated_data["receiver"]
        message = validated_data.get("message", "")

        quota = sender.kudos_quota
        quota.kudos_remaining -= 1
        quota.save()

        kudos = Kudos.objects.create(sender=sender, receiver=receiver, message=message)

        return kudos
