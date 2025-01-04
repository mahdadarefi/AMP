from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token







class UserRegister(APIView):
    def get(self,request):
        data=User.objects.all()
        ser_data=UserRegisterSerializer(instance=data,many=True)
        return Response(data=ser_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        ser_data=UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    seializer_class=UserLoginSerializer
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
            if user:
                token,created=Token.objects.get_or_create(user=user)
                return Response ({'token':[token.key],'success':'success Login user'},status=status.HTTP_201_CREATED)
            return Response({'message':'invalid username or passwoird'},status=status.HTTP_400_BAD_REQUEST)













