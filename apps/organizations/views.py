from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Membership
from .serializers import UserSerializer


class OrganizationUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user

        org_ids = Membership.objects.filter(user=current_user).values_list(
            "organization_id", flat=True
        )

        user_ids = Membership.objects.filter(organization_id__in=org_ids).values_list(
            "user_id", flat=True
        )

        users = (
            User.objects.filter(id__in=user_ids).exclude(id=current_user.id).distinct()
        )
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
