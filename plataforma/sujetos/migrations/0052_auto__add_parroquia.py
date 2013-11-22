# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parroquia'
        db.create_table(u'sujetos_parroquia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_parroquia', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'sujetos', ['Parroquia'])


    def backwards(self, orm):
        # Deleting model 'Parroquia'
        db.delete_table(u'sujetos_parroquia')


    models = {
        u'sujetos.cfs': {
            'Meta': {'object_name': 'cfs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cfs': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_estado': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'fk_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_municipio': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_parroquia': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.persona': {
            'CFS': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.cfs']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'condicion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'discapacidad': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'especifique': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'indigena': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numero_telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sujetos.Proyecto']", 'symmetrical': 'False', 'blank': 'True'}),
            'saberes': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'CFS': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.cfs']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Proyecto'},
            'comunidades': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'consejos_comunales': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_formativas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha_arranque': ('django.db.models.fields.DateField', [], {}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {}),
            'horas_contratadas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_dictadas_fecha': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_por_ejecutar': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'horas_proyectadas': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_inversion': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'numero_proyecto': ('django.db.models.fields.IntegerField', [], {}),
            'responsable_administrativo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_politico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sector_economico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['sujetos']