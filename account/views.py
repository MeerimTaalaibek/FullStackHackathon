from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from account import serializer
from account.send_mail import send_confirmation_email, send_reset_password
from account.serializer import PassResetApiSerializer, CreateNewPassSerializer

User = get_user_model()


class RegisterAPIView(APIView):

    def post(self, request):
        serializers = serializer.RegisterApiSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            if user:
                send_confirmation_email(user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'Успешно активирован!!'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'Sorry, ссылка устарела!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializer.LoginSerializer

class PassResetApiView(APIView):
    def post(self, request):
        serializer = PassResetApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(email=serializer.data.get('email'))
            user.is_active = False
            user.create_activation_code()
            user.save()
            send_reset_password(user)
            return Response('Проверьте почту!', status=200)
        return Response({'message': 'Пользователя с такой почтой не существует!'}, status=status.HTTP_400_BAD_REQUEST)


class NewPasswordApiView(APIView):
    def post(self, request):
        serializer = CreateNewPassSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Наконец-то, Вы успешно сменили пароль!', status=200)