# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Persona.proyecto'
        db.delete_column(u'sujetos_persona', 'proyecto_id')

        # Deleting field 'Persona.id'
        db.delete_column(u'sujetos_persona', 'id')


        # Changing field 'Persona.cedula'
        db.alter_column(u'sujetos_persona', 'cedula', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding unique constraint on 'Persona', fields ['cedula']
        db.create_unique(u'sujetos_persona', ['cedula'])

        # Adding field 'Proyecto.persona'
        db.add_column(u'sujetos_proyecto', 'persona',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sujetos.Persona']),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Persona', fields ['cedula']
        db.delete_unique(u'sujetos_persona', ['cedula'])

        # Adding field 'Persona.proyecto'
        db.add_column(u'sujetos_persona', 'proyecto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sujetos.Persona']),
                      keep_default=False)

        # Adding field 'Persona.id'
        db.add_column(u'sujetos_persona', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'Persona.cedula'
        db.alter_column(u'sujetos_persona', 'cedula', self.gf('django.db.models.fields.IntegerField')())
        # Deleting field 'Proyecto.persona'
        db.delete_column(u'sujetos_proyecto', 'persona_id')


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'sujetos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Persona']"})
        }
    }

    complete_apps = ['sujetos']