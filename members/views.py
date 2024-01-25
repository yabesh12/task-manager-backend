from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer

class UserSignupView(generics.CreateAPIView):
    """
    API endpoint for user registration.

    Allows users to sign up by providing a username, email, and password.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserLoginView(APIView):
    """
    API endpoint for user login.

    Allows users to log in by providing a username and password.
    Returns a token upon successful login.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user login.

        Parameters:
        - request: The HTTP request object.
        - args: Additional arguments passed to the view.
        - kwargs: Additional keyword arguments passed to the view.

        Returns:
        - Response: JSON response containing a token or an error message.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(f"{str(e)}")

class UserLogoutView(APIView):
    """
    API endpoint for user logout.

    Allows authenticated users to log out, deleting their authentication token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user logout.

        Parameters:
        - request: The HTTP request object.
        - args: Additional arguments passed to the view.
        - kwargs: Additional keyword arguments passed to the view.

        Returns:
        - Response: JSON response indicating successful logout or an error message.
        """
        # Delete the token associated with the user
        Token.objects.filter(user=request.user).delete()

        # Logout the user
        logout(request)

        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
