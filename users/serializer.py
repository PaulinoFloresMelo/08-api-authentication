from .models import Employee, User, Tbl_address, Tbl_organization
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tbl_address
		fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tbl_organization
		fields = '__all__'


class JoinUserEmployeeSerializer(serializers.Serializer):
    # user
	username = serializers.CharField(max_length=255)
	first_name = serializers.CharField(max_length=255)
	last_name = serializers.CharField(max_length=255)
	email = serializers.EmailField(max_length=255)
	is_staff = serializers.BooleanField()
	is_active = serializers.BooleanField()
	date_joined = serializers.DateTimeField()
	# employee
	user = serializers.IntegerField()                       # id
	rfc = serializers.CharField()                               # rfc (Registro Federal de Contribuyentes), sólo personas fisicas
	curp = serializers.CharField()                              # curp (Clave Única de Registro de Población)
	first_name = serializers.CharField( max_length=255)                                     # nombre/nombres de pila       
	middle_name = serializers.CharField( max_length=255)                                    # primer apellido        
	last_name = serializers.CharField( max_length=255)                                      # segundo apellido         
	trade_name = serializers.CharField( max_length=255)                                     # nombre Comercial
	start_operations = serializers.DateField()                                              # fecha inicio de operaciones   
	status_sat = serializers.BooleanField( default=False)                                   # estatus es el padrón SAT   
	last_change_status_sat_date = serializers.DateField( )                                  # fecha de último cambio de estado padrón SAT    
	registration_date = serializers.DateField( )                                            # fecha de registro (creación) en el sistema
	cancellation_date = serializers.DateField( )                                            # fecha de baja en el sistema
	last_updated_date = serializers.DateField( )