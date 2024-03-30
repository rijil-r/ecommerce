from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    The UserViewSet class is a viewset for the User model.

    Fields:
    queryset: The initial queryset that should be used for list views, and that should be used as the base for lookups of individual instances. It's set to all User objects.
    serializer_class: The serializer class used for the User model. It's set to UserSerializer.
    permission_classes: The permission classes for the viewset. It's set to IsAdminUser, which means only admin users can access this viewset.

    Methods:
    perform_create: Overrides the perform_create method to handle the creation of a new User instance.
    perform_update: Overrides the perform_update method to handle the update of a User instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        """
        Overrides the perform_create method to handle the creation of a new User instance.

        It extracts the password from the request data, saves the user without the password, and then sets the password if it's provided.
        If the password is not provided, it returns a 400 Bad Request response with an error message.
        """
        password = self.request.data.get('password')  # Extract password from request data
        user = serializer.save()  # Save the user without password
        if password:  # Check if password is provided
            user.set_password(password)  # Set the password
            user.save()  # Save the user with updated password
        else:
            return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        """
        Overrides the perform_update method to handle the update of a User instance.

        It extracts the password from the request data, saves the user without the password, and then sets the password if it's provided.
        """
        password = self.request.data.get('password')
        if password:
            user = serializer.save()
            user.set_password(password)
            user.save()