from django.urls import path

from gestionEmpleados import views 

urlpatterns = [
    path('home/', views.home, name="Home"),
    path('empleados/', views.empleados, name="Empleados"),
    path('departamentos/', views.departamentos, name="Departamentos"),
    path('empresas/', views.empresas, name="Empresas"),
    path('reportes/', views.reportes, name="Reportes"),
    path('registrar/', views.registrar_empleado,name="Registrar"),
    path('buscar/', views.buscar, name="Buscar"),
    path('editar/<int:id>', views.editar_empleado, name="Editar"),
    path('eliminar/', views.eliminar_empleado1, name="Eliminar"),
    path('eliminarE/<int:id>', views.eliminar_empleado, name="Borrar"),
    #empresas
    path('registrarEm/', views.registrar_empresa,name="RegistrarE"),
    path('buscarEm/', views.buscarE,name="BuscarE"),
    path('editarE/<int:id>', views.editar_empresa,name="EditarE"),
    path('registrarEm/<int:id>', views.eliminar_empresa,name="EliminarE"), 
    #deptos
    path('registrarD/', views.registrar_depto,name="RegistrarD"),
    path('buscarD/', views.buscarDept,name="BuscarD"),
    path('editarD/<int:id>', views.editar_depto,name="EditarD"),
    path('eliminarD/<int:id>', views.eliminar_depto,name="EliminarD"), 
    #Reportes
    path('reporteEmp/', views.re_emp, name="REmpresa"),
    path('reporteDep1/', views.re_dep, name="RDepto"),   #re_nom
    path('reportenom/', views.re_nom, name="RNombre"),
    
]