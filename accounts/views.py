from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import UserSerializer, UserSerializerWithToken,AddressSerializer
from rest_framework.response import Response
from .models import Address

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception:
        message = {'detail': 'User with this email already exists or data is not valid'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAddress(request):
    data = request.data
    try:
        address = AddressSerializer(data=data)
        if address.is_valid():
            address.save()
            return Response(address.data)
        else:
            return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        message = {'detail': 'Address is not valid'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAddress(request):
    address = request.user.get_Address()
    # address = Address.objects.filter(user=request.user)
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAddressById(request, pk):
    if(request.user!=Address.objects.get(id=pk).user):
        return Response("You are not authorized to access this address", status=status.HTTP_400_BAD_REQUEST)
    address = Address.objects.get(id=pk)
    serializer = AddressSerializer(address, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAddress(request, pk):
    if(request.user!=Address.objects.get(id=pk).user):
        return Response("You are not authorized to access this address", status=status.HTTP_400_BAD_REQUEST)
    address = Address.objects.get(id=pk)

    data = request.data

    address.address = data['address']
    address.city = data['city']
    address.postalCode = data['postalCode']
    address.country = data['country']
    # address.shippingAddress = data['shippingAddress']

    address.save()

    serializer = AddressSerializer(address, many=False)

    return Response(serializer.data)

@api_view(['DELETE','GET'])
@permission_classes([IsAuthenticated])
def deleteAddress(request, pk):
    if(request.user!=Address.objects.get(id=pk).user):
        return Response("You are not authorized to access this address", status=status.HTTP_400_BAD_REQUEST)
    addressForDeletion = Address.objects.get(id=pk)
    addressForDeletion.delete()
    return Response('Address was deleted')


