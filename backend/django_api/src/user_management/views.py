from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import UserDetailsSerializer


class UserManagement(viewsets.ModelViewSet):
   # authentication_classes = [TokenAuthentication]
   # permission_classes = [DjangoObjectPermissions]
   queryset = User.objects.all()
   serializer_class = UserDetailsSerializer


class CustomAuthToken(ObtainAuthToken):
   
   def post(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data,
                                         context={'request': request})
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data['user']
      token, created = Token.objects.get_or_create(user=user)
      return Response({
         'token': token.key,
         'user_id': user.pk,
         'email': user.email
      })


# class UserLogout(APIView):
#    authentication_classes = [TokenAuthentication]
#    # permission_classes = [IsAuthenticated]
#
#    def get(self, request):
#       request.user.auth_token.delete()
#       return Response({
#          'status': status.HTTP_200_OK,
#          'message': 'User logged out successfully',
#       })
