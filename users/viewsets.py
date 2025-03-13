from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Employee, User, Tbl_address, Tbl_organization
from .serializer import EmployeeSerializer, AddressSerializer, OrganizationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = EmployeeSerializer

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Tbl_address.objects.all()
	serializer_class = AddressSerializer
	permission_classes = [IsAuthenticated]

class OrganizationViewSet(viewsets.ModelViewSet):
	queryset = Tbl_organization.objects.all()
	serializer_class = OrganizationSerializer