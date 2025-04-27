from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serialzer import UserSerializer , CreateUserSerializerOutPut
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from categorys.models import Category, Idea
from categorys.serialzer import IdeaSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class UserView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={201: CreateUserSerializerOutPut},
    )
    def post(self,request):
        user_Serialized = UserSerializer(data = request.data)
        print(user_Serialized)
        if user_Serialized.is_valid():
            print('is hire ')
            user = user_Serialized.save()
            refresh = RefreshToken.for_user(user)
            out_data = CreateUserSerializerOutPut({
                'user':UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

            return Response(out_data.data,status=status.HTTP_200_OK )

        
        return Response(user_Serialized.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)