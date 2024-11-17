from rest_framework import generics
from custom_user_auth.models import UserProfile
from .serializers import UserProfileSerializers, RegistrationSerializer, CustomAuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        data = {
            'token': token.key,
            'id': user.id
        }
        
        return Response(data)    
 
 
# class RegisterView(APIView):
#     permission_classes = [AllowAny]  
    
#     data = {}

#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
        
#         email = data['email']
        
#         if not User.objects.filter(email=email).exists() and serializer.is_valid():
#             saved_account = serializer.save()
#             token, created = Token.objects.get_or_create(user=saved_account)
#             data = {
#                 'token': token.key,
#                 'username': saved_account.username,
#                 'email': saved_account.email,
#             }
#         else:
#             data= serializer.errors
            
#         return Response(data)
        
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Überprüfen, ob die E-Mail-Adresse existiert
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if not User.objects.filter(email=email).exists():
                # Benutzerkonto speichern und Token erstellen
                saved_account = serializer.save()
                token, _ = Token.objects.get_or_create(user=saved_account)
                return Response(
                    {
                        'token': token.key,
                        'username': saved_account.username,
                        'email': saved_account.email,
                    },
                    status=201,  # HTTP Statuscode: Created
                )
            else:
                return Response(
                    {'error': 'Ein Benutzer mit dieser E-Mail existiert bereits.'},
                    status=400,  # HTTP Statuscode: Bad Request
                )
        else:
            # Fehler des Serializers zurückgeben
            return Response(serializer.errors, status=400)      

       