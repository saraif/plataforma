# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Persona.proyecto'
        db.delete_column(u'sujetos_persona', 'proyecto_id')

        # Adding M2M table for field proyecto on 'Persona'
        m2m_table_name = db.shorten_name(u'sujetos_persona_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('persona', models.ForeignKey(orm[u'sujetos.persona'], null=False)),
            ('proyecto', models.ForeignKey(orm[u'sujetos.proyecto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['persona_id', 'proyecto_id'])


    def backwards(self, orm):
        # Adding field 'Persona.proyecto'
        db.add_column(u'sujetos_persona', 'proyecto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sujetos.Proyecto']),
                      keep_default=False)

        # Removing M2M table for field proyecto on 'Persona'
        db.delete_table(db.shorten_name(u'sujetos_persona_proyecto'))


    models = {
        u'sujetos.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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