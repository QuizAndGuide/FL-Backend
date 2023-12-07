from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer

class CreateUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserCreateSerializer(data=request.data)

        if user_serializer.is_valid():
            # Guardar el usuario
            user = user_serializer.save()

            return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)