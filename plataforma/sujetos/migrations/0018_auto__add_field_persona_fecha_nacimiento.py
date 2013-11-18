# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
import datetime


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Persona.fecha_nacimiento'
        db.add_column(u'sujetos_persona', 'fecha_nacimiento',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today()),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Persona.fecha_nacimiento'
        db.delete_column(u'sujetos_persona', 'fecha_nacimiento')


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sujetos.Proyecto']", 'symmetrical': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['sujetos']