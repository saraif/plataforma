# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Persona.numero_telefono'
        db.add_column(u'sujetos_persona', 'numero_telefono',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Persona.telefono'
        db.alter_column(u'sujetos_persona', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=1))

    def backwards(self, orm):
        # Deleting field 'Persona.numero_telefono'
        db.delete_column(u'sujetos_persona', 'numero_telefono')


        # Changing field 'Persona.telefono'
        db.alter_column(u'sujetos_persona', 'telefono', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numero_telefono': ('django.db.models.fields.IntegerField', [], {}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sujetos.Proyecto']", 'symmetrical': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': '278', 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['sujetos']