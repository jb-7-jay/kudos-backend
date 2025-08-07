from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import KudosCreateSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


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
