from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from gestionEmpleados.models import Empleado
from gestionEmpleados.models import Empresa
from gestionEmpleados.models import Departamento

# Create your views here.

#------Paginas Prinicpales 

def index(request):
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def empleados(request):
    return render(request,"empleados.html")

def departamentos(request):
    return render(request,"departamentos.html")

def empresas(request):
    return render(request,"empresas.html")

def reportes(request):
    return render(request,"reportes.html")

#--------Maenjo de empledaos 
def editar_empleado(request,id):
    empleado = Empleado.objects.get(id=id)
    
    if request.method == 'GET':
        return render(request,"editar_empleado.html",{"empleado":empleado})
    else:
        if request.method == "POST":
            d1=request.POST["name"]
            d2=request.POST["nacimiento"]
            d3=request.POST["mail"]
            d4=request.POST["genero"]
            d5=request.POST["tel"]
            d6=request.POST["cel"]
            d7=request.POST["depto"]
    
            empleado1 = Empleado(id=id,nombre=d1,fechanac=d2,email=d3,genero=d4,telefono=d5,cel=d6,fechaing=empleado.fechaing,depto_id=d7)
            empleado1.save();
            
    lista = Empleado.objects.all()
    return render(request,"resultados_busqueda.html",{"articulos":lista})



def eliminar_empleado(request,id):
    empleado = Empleado.objects.get(id=id)
    
    if request.method == 'GET':
        empleado.delete()
    
    lista = Empleado.objects.all()    
    return render(request,"resultados_eliminar.html",{"articulos":lista})

def registrar_empleado(request):
    deptos = Departamento.objects.all()
    return render(request,"registro_empleados.html",{"departamentos":deptos})


def buscar(request):
    #b = Book.objects.select_related('author__hometown').get(id=4)
    lista = Empleado.objects.all()
    
    return render(request,"resultados_busqueda.html",{"articulos":lista})

def eliminar_empleado1(request):
    
    lista = Empleado.objects.all()
    
    return render(request,"resultados_eliminar.html",{"articulos":lista})
    
def registroE(request):
    lista = Empleado.objects.all()
    if request.method == "POST":
        d1=request.POST["name"]
        d2=request.POST["nacimiento"]
        d3=request.POST["mail"]
        d4=request.POST["genero"]
        d5=request.POST["tel"]
        d6=request.POST["cel"]
        d7=request.POST["ingreso"]
        d8=request.POST["depto"]
    
        empleado = Empleado(nombre=d1,fechanac=d2,email=d3,genero=d4,telefono=d5,cel=d6,fechaing=d7,depto_id=d8)
        empleado.save();
    return render(request,"resultados_busqueda.html",{"articulos":lista})



#---------------------------Manejo de Empresas 

def registrar_empresa(request):
    return render(request,"registro_empresa.html")

def registroEm(request):
    
    lista = Empresa.objects.all()
    if request.method == "POST":
        d1=request.POST["name"]
        d2=request.POST["contact"]
        d5=request.POST["dir"]
        d6=request.POST["tel"]
    
        empresa = Empresa(nombre=d1,contacto=d2,direccion=d5,telefono=d6)
        empresa.save();
    return render(request,"resultados_empresas.html",{"articulos":lista})


def buscarE(request):
    #b = Book.objects.select_related('author__hometown').get(id=4)
    lista = Empresa.objects.all()
    
    return render(request,"resultados_empresas.html",{"articulos":lista})


def editar_empresa(request,id):
    emp = Empresa.objects.get(id=id)
    
    if request.method == 'GET':
        return render(request,"editar_empresa.html",{"empresa":emp})
    else:
        if request.method == "POST":
            d1=request.POST["name"]
            d2=request.POST["contact"]
            d5=request.POST["dir"]
            d6=request.POST["tel"]
    
            empresa = Empresa(nombre=d1,contacto=d2,direccion=d5,telefono=d6,id=emp.id)
            empresa.save();
            
    lista = Empresa.objects.all()
    return render(request,"resultados_empresas.html",{"articulos":lista})

def eliminar_empresa(request,id):
    empresa = Empresa.objects.get(id=id)
    
    if request.method == 'GET':
        empresa.delete()
    
    lista = Empresa.objects.all()    
    return render(request,"resultados_empresas.html",{"articulos":lista})


#------------------Manejo de Departamentos 

def registrar_depto(request):
    lista = Empresa.objects.all() 
    listaE = Empleado.objects.all()
    return render(request,"registro_depto.html",{"empresas":lista})

def buscarDept(request):
    #b = Book.objects.select_related('author__hometown').get(id=4)
    lista = Departamento.objects.all()
    #deptos = Departamento.objects.all().select_related('parametro')
    
    return render(request,"resultados_deptos.html",{"articulos":lista})

def registroDep(request):
    
    depto = Departamento.objects.all()
    if request.method == "POST":
        d1=request.POST["name"]
        d5=request.POST["emp"]
    
        depto1 = Departamento(nombre=d1,emp_id=d5)
        depto1.save();
    return render(request,"resultados_deptos.html",{"articulos":depto})

def editar_depto(request,id):
    depto = Departamento.objects.get(id=id)
    emp = Empresa.objects.get(id=depto.emp_id)
    
    if request.method == 'GET':
        return render(request,"editar_depto.html",{"departamento":depto,"empresa":emp})
    else:
        if request.method == "POST":
            d1=request.POST["name"]
            d2=request.POST["resp"]
            d5=request.POST["emp1"]
    
            depto1 = Departamento(nombre=d1,emp_id=d5,responsable=d2,id=id)
            depto1.save();
            
    deptos = Departamento.objects.all()
    return render(request,"resultados_deptos.html",{"articulos":deptos})


def eliminar_depto(request,id):
    depto = Departamento.objects.get(id=id)
    
    if request.method == 'GET':
        depto.delete()
    
    deptos = Departamento.objects.all()
    return render(request,"resultados_deptos.html",{"articulos":deptos})


#----------------reportes

def re_emp(request):
    
    lista = Empresa.objects.all() 
    
    return render(request,"reporte_empresa.html",{"empleados":"","empresas":lista})
    

def rep_empe(request):
    query=""
    lista=""
    if request.method == "POST":
        d5=request.POST["emp"]
        query = Empleado.objects.raw('SELECT DISTINCT e.id, e.nombre as Empleado, dep.id, dep.nombre as Departamento from gestionEmpleados_empresa emp, gestionEmpleados_departamento dep , gestionEmpleados_empleado e where e.depto_id=dep.id AND dep.emp_id='+d5)
        lista = Empresa.objects.all() 
         
    
    return render(request,"reporte_empresa.html",{"empleados":query,"empresas":lista})


def re_dep(request):
    
    lista = Departamento.objects.all() 
    return render(request,"reporte_depto.html",{"empleados":"","deptos":lista})


def rep_d(request):
    query=""
    lista=""
    if request.method == "POST":
        d5=request.POST["dep"]
        query = Empleado.objects.raw('SELECT e.id, e.nombre as Empleado from gestionEmpleados_empleado e where e.depto_id='+d5)
        lista = Departamento.objects.all() 
        return render(request,"reporte_depto.html",{"empleados":query,"deptos":lista})
         
    
    return render(request,"reporte_depto.html",{"empleados":query,"deptos":lista})

def re_nom(request):
    
    lista = Empleado.objects.all() 
    return render(request,"reporte_nombre.html",{"empleados":lista})


def re_nombre(request):
    
    lista = Empleado.objects.all() 
    if request.method == "POST":
        d5=request.POST["nombre"]
        query = Empleado.objects.raw("SELECT * from gestionEmpleados_empleado where nombre LIKE '%"+d5+"%'")
        #return render(request,"reporte_nombre.html",{"empleados":query)
         
    return render(request,"reporte_nombre.html",{"empleado":query,"empleados":lista})