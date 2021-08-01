from django.contrib import admin


from gestionEmpleados.models import Empleado
from gestionEmpleados.models import Departamento
from gestionEmpleados.models import Empresa

# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display= ("nombre","email","fechaing","depto")
    search_fields=("nombre","email")
    list_filter=("nombre","fechaing")
    date_hierarchy=("fechaing")

class DepartamentoAdmin(admin.ModelAdmin):
        list_display= ("nombre","emp")
        search_fields=("nombre",)
        
class EmpresaAdmin(admin.ModelAdmin):
        list_display= ("id","nombre")
        search_fields=("nombre",)

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Empresa, EmpresaAdmin)

