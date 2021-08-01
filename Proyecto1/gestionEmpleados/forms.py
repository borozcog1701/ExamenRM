from django import forms

DEMO_CHOICES =(
    ("", "Selecciona..."),
    ("H", "Hombre"),
    ("M", "Mujer"),
)

class FormularioEmpleado(forms.Form):
    nombre=forms.CharField()
    fechan=forms.DateField()
    email=forms.EmailField()
    genero=forms.MultipleChoiceField(choices = DEMO_CHOICES)
    tel=forms.CharField()
    cel=forms.CharField()
    fechai=forms.DateField()