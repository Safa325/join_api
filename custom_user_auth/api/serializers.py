from rest_framework import serializers
from custom_user_auth.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email']

       
class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
       
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    def validate_email(self):
        email = self.validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Diese E-Mail-Adresse ist bereits registriert.")
        return email

    def save(self):
        pw = self.validated_data['password']
        repeated_password = self.validated_data['repeated_password']
        
        if pw != repeated_password:
            raise serializers.ValidationError({'error':'password dont match!'})
      
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account
    
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError("Invalid email/password combination.")
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email/password combination.")

        
        attrs['user'] = user
        return attrs    