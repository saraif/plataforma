# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Persona.proyecto'
        db.add_column(u'sujetos_persona', 'proyecto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sujetos.Proyecto']),
                      keep_default=False)

        # Deleting field 'Proyecto.persona'
        db.delete_column(u'sujetos_proyecto', 'persona_id')


    def backwards(self, orm):
        # Deleting field 'Persona.proyecto'
        db.delete_column(u'sujetos_persona', 'proyecto_id')

        # Adding field 'Proyecto.persona'
        db.add_column(u'sujetos_proyecto', 'persona',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sujetos.Persona']),
                      keep_default=False)


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Proyecto']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['sujetos']