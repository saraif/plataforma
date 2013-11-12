# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Persona.indigena'
        db.add_column(u'sujetos_persona', 'indigena',
                      self.gf('django.db.models.fields.CharField')(default='N', max_length=1),
                      keep_default=False)

        # Adding field 'Persona.discapacidad'
        db.add_column(u'sujetos_persona', 'discapacidad',
                      self.gf('django.db.models.fields.CharField')(default='N', max_length=1),
                      keep_default=False)

        # Adding field 'Persona.especifique'
        db.add_column(u'sujetos_persona', 'especifique',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=60),
                      keep_default=False)

        # Adding field 'Persona.condicion'
        db.add_column(u'sujetos_persona', 'condicion',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=60),
                      keep_default=False)

        # Adding field 'Persona.saberes'
        db.add_column(u'sujetos_persona', 'saberes',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=60),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Persona.indigena'
        db.delete_column(u'sujetos_persona', 'indigena')

        # Deleting field 'Persona.discapacidad'
        db.delete_column(u'sujetos_persona', 'discapacidad')

        # Deleting field 'Persona.especifique'
        db.delete_column(u'sujetos_persona', 'especifique')

        # Deleting field 'Persona.condicion'
        db.delete_column(u'sujetos_persona', 'condicion')

        # Deleting field 'Persona.saberes'
        db.delete_column(u'sujetos_persona', 'saberes')


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'condicion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'discapacidad': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'especifique': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'indigena': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numero_telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sujetos.Proyecto']", 'symmetrical': 'False', 'blank': 'True'}),
            'saberes': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'numero_proyecto': ('django.db.models.fields.IntegerField', [], {}),
            'parroquia': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_administrativo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_politico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sector_economico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['sujetos']