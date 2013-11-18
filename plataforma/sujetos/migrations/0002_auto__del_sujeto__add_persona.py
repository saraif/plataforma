# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Sujeto'
        db.delete_table(u'sujetos_sujeto')

        # Adding model 'Persona'
        db.create_table(u'sujetos_persona', (
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('sexo', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
            ('cedula', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Proyecto'])),
        ))
        db.send_create_signal(u'sujetos', ['Persona'])


    def backwards(self, orm):
        # Adding model 'Sujeto'
        db.create_table(u'sujetos_sujeto', (
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('sexo', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Proyecto'])),
            ('cedula', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
        ))
        db.send_create_signal(u'sujetos', ['Sujeto'])

        # Deleting model 'Persona'
        db.delete_table(u'sujetos_persona')


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
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