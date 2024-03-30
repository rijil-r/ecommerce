from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        password = self.request.data.get('password')  # Extract password from request data
        user = serializer.save()  # Save the user without password
        if password:  # Check if password is provided
            user.set_password(password)  # Set the password
            user.save()  # Save the user with updated password
        else:
            return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        password = self.request.data.get('password')
        if password:
            user = serializer.save()
            user.set_password(password)
            user.save()

