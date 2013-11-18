from django.db import models
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

# Comentario de prueba

class Persona(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_CHOICES = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    )
  
    SI = 'S'
    NO = 'N'
    DISCAPACIDAD_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )
    
    SI = 'S'
    NO = 'N'
    INDIGENA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )
  
  
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    cedula = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField() 
    sexo = models.CharField(max_length=1,
                            choices=SEXO_CHOICES,
                            default=FEMENINO)
    
    CFS = models.ForeignKey('cfs', null=True, blank=True)

    estado = models.ForeignKey('Estado', null=True, blank=True)
    municipio = models.ForeignKey('Municipio', null=True, blank=True)
    parroquia = models.CharField(max_length=60, blank=False)
    numero_telefono = models.CharField(max_length=60, blank=False)
    correo_electronico = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=60)
    indigena = models.CharField(max_length=1,
                            choices=INDIGENA_CHOICES,
                            default=NO)
    
    discapacidad = models.CharField(max_length=1,
                            choices=DISCAPACIDAD_CHOICES,
                            default=NO)
    especifique = models.CharField(max_length=60, null=True, blank=True)                        
    condicion = models.CharField(max_length=60)
    saberes = models.CharField(max_length=60)
    proyecto = models.ManyToManyField('Proyecto', blank=True)
    
    
    def __unicode__(self):
        return self.nombres
        

        
    def proyecto_asociado(self):
        return "\n".join([n.nombre for n in self.proyecto.all()])
        nombre.short_description = "Proyecto Asociado"

class PersonaAdmin(admin.ModelAdmin):
    list_display = ["proyecto_asociado","nombres", "apellidos", "sexo", "cedula", "edad", "condicion"]
    search_fields = ["cedula", "nombres"]
    list_filter = ('condicion','proyecto', 'edad', 'sexo')

    
    
    
class Proyecto(models.Model):
    numero_proyecto = models.IntegerField()
    nombre = models.CharField(max_length = 10)
    CFS = models.ForeignKey('cfs', null=True, blank=True)
    estado = models.ForeignKey('Estado', null=True, blank=True)
    municipio = models.ForeignKey('Municipio', null=True, blank=True)
    parroquia = models.CharField(max_length = 30, null=False)
    comunidades = models.CharField(max_length = 30, null=False)
    consejos_comunales = models.CharField(max_length = 30, null=False)
    ubicacion = models.CharField(max_length = 30, null=False)
    horas_dictadas_fecha = models.CharField(max_length = 30, null=False)
    horas_por_ejecutar = models.CharField(max_length = 30, null=False)
    horas_contratadas = models.CharField(max_length = 30, null=False)
    horas_proyectadas = models.CharField(max_length = 30, null=False)
    monto_inversion = models.IntegerField(null=False)
    fecha_arranque = models.DateField()
    fecha_finalizacion = models.DateField()
    estatus = models.CharField(max_length = 30, null=False)
    responsable_politico = models.CharField(max_length = 30, null=False)
    responsable_administrativo = models.CharField(max_length = 30, null=False)
    tipo_proyecto = models.CharField(max_length = 30, null=False)
    sector_economico = models.CharField(max_length = 30, null=False)
    dimensiones_formativas = models.CharField(max_length = 30, null=False)
    
    
    def __unicode__(self):
        return self.nombre


class Estado(models.Model):
    nombre_estado = models.CharField(max_length = 10)
    
    def __unicode__(self):
        return self.nombre_estado
        


class EstadoAdmin(admin.ModelAdmin):
    list_display = ["nombre_estado"]


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length = 60)
    
    def __unicode__(self):
        return self.nombre_municipio
        

    
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ["nombre_municipio"]
    
    
class cfs(models.Model):
    nombre_cfs = models.CharField(max_length = 60)
    
    def __unicode__(self):
        return self.nombre_cfs
        

    
class cfsAdmin(admin.ModelAdmin):
    list_display =["nombre_cfs"]

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Proyecto)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(cfs, cfsAdmin)
