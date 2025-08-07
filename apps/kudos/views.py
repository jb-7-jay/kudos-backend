from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import KudosCreateSerializer, KudosSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Kudos


class KudosCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = KudosCreateSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Kudos sent successfully",
                },
                status=HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class KudosActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        send_kudos = Kudos.objects.filter(sender=user).order_by("-created_at")
        received_kudos = Kudos.objects.filter(receiver=user).order_by("-created_at")

        send_serializer = KudosSerializer(send_kudos, many=True)
        received_serializer = KudosSerializer(received_kudos, many=True)

        return Response(
            {"send": send_serializer.data, "received": received_serializer.data}
        )
