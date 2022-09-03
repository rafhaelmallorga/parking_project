from rest_framework.views import APIView, Request, Response, status

from .models import Account
from .serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        users = Account.objects.all()
        serializer = RegisterSerializer(users, many=True)

        return Response(serializer.data)
