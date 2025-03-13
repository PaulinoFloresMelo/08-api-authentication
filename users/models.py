from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

import django.utils.timezone

class Tbl_address(models.Model):
    addr_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name="address id") # id
    zip_code = models.CharField(max_length=32)                  # código postal     - ver 'CatCFDI_V_20240619.xlsx' pestaña 'c_CodigoPostal_Parte_1' y 'c_CodigoPostal_Parte_2'
    name_roadway = models.CharField(max_length=150)             # tipo de vialidad
    ins_number = models.CharField(max_length=10)                # número interior 'inside_number'
    locality = models.CharField(max_length=10)                  # localidad
    federal_entity = models.CharField(max_length=70)            # entidad federativa o estado
    type_road = models.CharField(max_length=100)                # tipo de vialidad
    out_number = models.CharField(max_length=10)                # número exterior 'outside_number'
    neighborhood = models.CharField(max_length=100)             # nombre de colonia, barrio o vecindario
    municipality = models.CharField(max_length=100)             # nombre del municipio o demarcación territorial
    ref_btw_st = models.CharField(max_length=100)               # referencia entre calle - 'reference_between_street'
    ref_and_st = models.CharField(max_length=100)               # referencia y calle - 'reference_and_street'

    def __str__(self):
        return f"{self.neighborhood} -id: {self.addr_id}"

class Tbl_organization(models.Model): 
    org_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name="organization id")
    rfc = models.CharField(max_length=12)
    company_name = models.CharField(max_length=254)
    capital_regime = models.CharField(max_length=250)
    trade_name = models.CharField(max_length=250)
    start_operations = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    status_sat = models.BooleanField()
    path_csf  = models.CharField(max_length=255)
    ase_key = models.CharField(max_length=10)
    asf_key = models.CharField(max_length=10)
    admin_period = models.CharField(max_length=15)
    last_change_status_sat_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    registration_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    cancellation_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    last_updated_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')

    def __str__(self):
        return f"{self.company_name} -id: {self.org_id}"
    


class User(AbstractUser):
    email = models.CharField( unique=True, max_length=255)
    username = models.CharField( unique= False, max_length=255,)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        "username",
        ]
    
    def __str__(self):
         return self.email
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, )
    empl_id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name="Employee id") # id
    rfc = models.CharField( max_length=13, validators=[MinLengthValidator(13)])        # rfc (Registro Federal de Contribuyentes), sólo personas fisicas
    curp = models.CharField( max_length=18, validators=[MinLengthValidator(18)])       # curp (Clave Única de Registro de Población)
    first_name = models.CharField( max_length=255)                                     # nombre/nombres de pila       
    middle_name = models.CharField( max_length=255)                                    # primer apellido        
    last_name = models.CharField( max_length=255)                                      # segundo apellido         
    trade_name = models.CharField( max_length=255)                                     # nombre Comercial
    start_operations = models.DateField()                                              # fecha inicio de operaciones   
    status_sat = models.BooleanField( default=False)                                   # estatus es el padrón SAT   
    last_change_status_sat_date = models.DateField( )                                  # fecha de último cambio de estado padrón SAT    
    registration_date = models.DateField( )                                            # fecha de registro (creación) en el sistema
    cancellation_date = models.DateField( )                                            # fecha de baja en el sistema
    last_updated_date = models.DateField( )                                            # fecha de creación       

    