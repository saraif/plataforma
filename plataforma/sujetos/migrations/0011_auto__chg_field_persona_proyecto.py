# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Persona.proyecto'
        db.alter_column(u'sujetos_persona', 'proyecto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Persona']))

    def backwards(self, orm):

        # Changing field 'Persona.proyecto'
        db.alter_column(u'sujetos_persona', 'proyecto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Proyecto']))

    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'default': '0', 'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Persona']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['sujetos']