from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializer import EmployeeSerializer, UserSerializer, JoinUserEmployeeSerializer
from .models import Employee, User

# 12qw34er56??
def create_user(userData):
    email = userData['email']
    serializer = UserSerializer( data = userData)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get( email = serializer.data['email'] )
        user.set_password(serializer.data['password'])
        user.save()
        return user
    else: 
        try:
            user = User.objects.get( email = email )
            print(serializer.errors)
            return user
        except User.DoesNotExist:
            print("El usuario no existe.")
        except User.MultipleObjectsReturned:
            print("Se encontraron múltiples objetos.")


# to do: estoy trabajando en esto no está funcionado de la manera adecuada
def create_employee(employeeData):
    serializer = EmployeeSerializer( data = employeeData)
    if serializer.is_valid():
        serializer.save()
        employee = Employee.objects.get( empl_id = serializer.data['empl_id'] )
        return employee
    else: 
        try:
            user = User.objects.get( id= employeeData['user'] )
            print(serializer.errors)
            return user
        except User.DoesNotExist:
            print("El usuario no existe.")
        except User.MultipleObjectsReturned:
            print("Se encontraron múltiples objetos.")

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    # user = get_object_or_404(Employee, email = request.data['email'])
    try:
        user = User.objects.get(email = request.data['email'])
        if (user):
            userAutheticated = authenticate(
                email= request.data['email'],
                password= request.data['password'])
            print(request.data['email'])
            if not userAutheticated:
                return Response({"error": "Ivalid credentials"}, status= status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(instance = user)
            user = {
                'id' :serializer.data['id'],
                'email' :serializer.data['email'],
                'username': serializer.data['username'],
                'isActive': serializer.data['is_active'],
                'roles': serializer.data['groups'],
                }
            return Response({
                "user": user,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
                },
                status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error" : "Ivalid credentials"}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_token(request):
    JWT_authenticator = JWTAuthentication()
    # token = extract_token_from_header(request)
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        # unpacking
        user , token = response
        serializer = UserSerializer(instance = user)

        user = {
            'id' :serializer.data['id'],
            'email' :serializer.data['email'],
            'username': serializer.data['username'],
            'isActive': serializer.data['is_active'],
            'roles': serializer.data['groups'],
        }
        return Response({
            'user': user,
            'access': str(token),
            'validated': True,
            },
        status=status.HTTP_200_OK)
    else:
        print("no token is provided in the header or the header is missing")
    
        return Response({'validated': False},
        status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def register_employee(request):
    
    serializer = JoinUserEmployeeSerializer( data= request.data)
    print(serializer)
    if serializer.is_valid():
        user = create_user(request.data)
        employee = create_employee(request.data)
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": serializer.data['email'],
            "refresh": str(refresh),
            "access": str(refresh.access_token)
            }, 
            status= status.HTTP_201_CREATED)
    return Response( serializer.errors, status= status.HTTP_400_BAD_REQUEST)
