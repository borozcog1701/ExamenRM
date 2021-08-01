from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50, blank=True,null=True)
    telefono=models.CharField(max_length=10, blank=True,null=True)
    direccion=models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.nombre
    
class  Departamento(models.Model):
    nombre=models.CharField(max_length=50)
    emp=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
    
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    fechanac=models.DateField(verbose_name="Fecha de Nacimiento")
    email=models.EmailField()
    genero=models.CharField(max_length=5, blank=True,null=True)
    telefono=models.CharField(max_length=10,blank=True,null=True)
    cel=models.CharField(max_length=10,blank=True,null=True)
    fechaing=models.DateField(verbose_name="Fecha de Ingreso")
    depto=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    

    


    