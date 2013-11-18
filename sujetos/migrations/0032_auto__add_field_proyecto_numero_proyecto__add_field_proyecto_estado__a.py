# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proyecto.numero_proyecto'
        db.add_column(u'sujetos_proyecto', 'numero_proyecto',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Proyecto.estado'
        db.add_column(u'sujetos_proyecto', 'estado',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.municipio'
        db.add_column(u'sujetos_proyecto', 'municipio',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.parroquia'
        db.add_column(u'sujetos_proyecto', 'parroquia',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.comunidades'
        db.add_column(u'sujetos_proyecto', 'comunidades',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.consejos_comunales'
        db.add_column(u'sujetos_proyecto', 'consejos_comunales',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.ubicacion'
        db.add_column(u'sujetos_proyecto', 'ubicacion',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.horas_dictadas_fecha'
        db.add_column(u'sujetos_proyecto', 'horas_dictadas_fecha',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.horas_por_ejecutar'
        db.add_column(u'sujetos_proyecto', 'horas_por_ejecutar',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.horas_contratadas'
        db.add_column(u'sujetos_proyecto', 'horas_contratadas',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.horas_proyectadas'
        db.add_column(u'sujetos_proyecto', 'horas_proyectadas',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.monto_inversion'
        db.add_column(u'sujetos_proyecto', 'monto_inversion',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Proyecto.fecha_arranque'
        db.add_column(u'sujetos_proyecto', 'fecha_arranque',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today()),
                      keep_default=False)

        # Adding field 'Proyecto.fecha_finalizacion'
        db.add_column(u'sujetos_proyecto', 'fecha_finalizacion',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today()),
                      keep_default=False)

        # Adding field 'Proyecto.estatus'
        db.add_column(u'sujetos_proyecto', 'estatus',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.responsable_politico'
        db.add_column(u'sujetos_proyecto', 'responsable_politico',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.responsable_administrativo'
        db.add_column(u'sujetos_proyecto', 'responsable_administrativo',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.tipo_proyecto'
        db.add_column(u'sujetos_proyecto', 'tipo_proyecto',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.sector_economico'
        db.add_column(u'sujetos_proyecto', 'sector_economico',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.dimensiones_formativas'
        db.add_column(u'sujetos_proyecto', 'dimensiones_formativas',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)


        # Changing field 'Proyecto.nombre'
        db.alter_column(u'sujetos_proyecto', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Deleting field 'Proyecto.numero_proyecto'
        db.delete_column(u'sujetos_proyecto', 'numero_proyecto')

        # Deleting field 'Proyecto.estado'
        db.delete_column(u'sujetos_proyecto', 'estado')

        # Deleting field 'Proyecto.municipio'
        db.delete_column(u'sujetos_proyecto', 'municipio')

        # Deleting field 'Proyecto.parroquia'
        db.delete_column(u'sujetos_proyecto', 'parroquia')

        # Deleting field 'Proyecto.comunidades'
        db.delete_column(u'sujetos_proyecto', 'comunidades')

        # Deleting field 'Proyecto.consejos_comunales'
        db.delete_column(u'sujetos_proyecto', 'consejos_comunales')

        # Deleting field 'Proyecto.ubicacion'
        db.delete_column(u'sujetos_proyecto', 'ubicacion')

        # Deleting field 'Proyecto.horas_dictadas_fecha'
        db.delete_column(u'sujetos_proyecto', 'horas_dictadas_fecha')

        # Deleting field 'Proyecto.horas_por_ejecutar'
        db.delete_column(u'sujetos_proyecto', 'horas_por_ejecutar')

        # Deleting field 'Proyecto.horas_contratadas'
        db.delete_column(u'sujetos_proyecto', 'horas_contratadas')

        # Deleting field 'Proyecto.horas_proyectadas'
        db.delete_column(u'sujetos_proyecto', 'horas_proyectadas')

        # Deleting field 'Proyecto.monto_inversion'
        db.delete_column(u'sujetos_proyecto', 'monto_inversion')

        # Deleting field 'Proyecto.fecha_arranque'
        db.delete_column(u'sujetos_proyecto', 'fecha_arranque')

        # Deleting field 'Proyecto.fecha_finalizacion'
        db.delete_column(u'sujetos_proyecto', 'fecha_finalizacion')

        # Deleting field 'Proyecto.estatus'
        db.delete_column(u'sujetos_proyecto', 'estatus')

        # Deleting field 'Proyecto.responsable_politico'
        db.delete_column(u'sujetos_proyecto', 'responsable_politico')

        # Deleting field 'Proyecto.responsable_administrativo'
        db.delete_column(u'sujetos_proyecto', 'responsable_administrativo')

        # Deleting field 'Proyecto.tipo_proyecto'
        db.delete_column(u'sujetos_proyecto', 'tipo_proyecto')

        # Deleting field 'Proyecto.sector_economico'
        db.delete_column(u'sujetos_proyecto', 'sector_economico')

        # Deleting field 'Proyecto.dimensiones_formativas'
        db.delete_column(u'sujetos_proyecto', 'dimensiones_formativas')


        # Changing field 'Proyecto.nombre'
        db.alter_column(u'sujetos_proyecto', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=60))

    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numero_telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sujetos.Proyecto']", 'symmetrical': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'comunidades': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'consejos_comunales': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_formativas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha_arranque': ('django.db.models.fields.DateField', [], {}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {}),
            'horas_contratadas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_dictadas_fecha': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_por_ejecutar': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_proyectadas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero_proyecto': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parroquia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_administrativo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_politico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sector_economico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['sujetos']