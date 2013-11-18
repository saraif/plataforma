# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'cfs'
        db.create_table(u'sujetos_cfs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_cfs', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'sujetos', ['cfs'])

        # Adding model 'Parroquia'
        db.create_table(u'sujetos_parroquia', (
            ('id_Parroquia', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('fk_municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Municipio'], null=True, blank=True)),
            ('nombre_parroquia', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'sujetos', ['Parroquia'])

        # Adding model 'Estado'
        db.create_table(u'sujetos_estado', (
            ('id_Estado', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre_estado', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'sujetos', ['Estado'])

        # Adding model 'Municipio'
        db.create_table(u'sujetos_municipio', (
            ('nombre_municipio', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('id_municipio', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('fk_estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Estado'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sujetos', ['Municipio'])

        # Adding field 'Persona.CFS'
        db.add_column(u'sujetos_persona', 'CFS',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=60),
                      keep_default=False)

        # Adding field 'Persona.parroquia'
        db.add_column(u'sujetos_persona', 'parroquia',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Municipio'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Proyecto.estado'
        db.delete_column(u'sujetos_proyecto', 'estado')

        # Deleting field 'Proyecto.municipio'
        db.delete_column(u'sujetos_proyecto', 'municipio')

        # Adding field 'Proyecto.CFS'
        db.add_column(u'sujetos_proyecto', 'CFS',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.cfs'], null=True, blank=True),
                      keep_default=False)


        # Renaming column for 'Proyecto.parroquia' to match new field type.
        db.rename_column(u'sujetos_proyecto', 'parroquia', 'parroquia_id')
        # Changing field 'Proyecto.parroquia'
        db.alter_column(u'sujetos_proyecto', 'parroquia_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sujetos.Municipio'], null=True))
        # Adding index on 'Proyecto', fields ['parroquia']
        db.create_index(u'sujetos_proyecto', ['parroquia_id'])


    def backwards(self, orm):
        # Removing index on 'Proyecto', fields ['parroquia']
        db.delete_index(u'sujetos_proyecto', ['parroquia_id'])

        # Deleting model 'cfs'
        db.delete_table(u'sujetos_cfs')

        # Deleting model 'Parroquia'
        db.delete_table(u'sujetos_parroquia')

        # Deleting model 'Estado'
        db.delete_table(u'sujetos_estado')

        # Deleting model 'Municipio'
        db.delete_table(u'sujetos_municipio')

        # Deleting field 'Persona.CFS'
        db.delete_column(u'sujetos_persona', 'CFS')

        # Deleting field 'Persona.parroquia'
        db.delete_column(u'sujetos_persona', 'parroquia_id')

        # Adding field 'Proyecto.estado'
        db.add_column(u'sujetos_proyecto', 'estado',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Proyecto.municipio'
        db.add_column(u'sujetos_proyecto', 'municipio',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Deleting field 'Proyecto.CFS'
        db.delete_column(u'sujetos_proyecto', 'CFS_id')


        # Renaming column for 'Proyecto.parroquia' to match new field type.
        db.rename_column(u'sujetos_proyecto', 'parroquia_id', 'parroquia')
        # Changing field 'Proyecto.parroquia'
        db.alter_column(u'sujetos_proyecto', 'parroquia', self.gf('django.db.models.fields.CharField')(default=0, max_length=30))

    models = {
        u'sujetos.cfs': {
            'Meta': {'object_name': 'cfs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cfs': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.estado': {
            'Meta': {'object_name': 'Estado'},
            'id_Estado': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre_estado': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'fk_estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Estado']", 'null': 'True', 'blank': 'True'}),
            'id_municipio': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre_municipio': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            'fk_municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Municipio']", 'null': 'True', 'blank': 'True'}),
            'id_Parroquia': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre_parroquia': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'sujetos.persona': {
            'CFS': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'condicion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'discapacidad': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'especifique': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'indigena': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'numero_telefono': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'parroquia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Municipio']", 'null': 'True', 'blank': 'True'}),
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
            'parroquia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sujetos.Municipio']", 'null': 'True', 'blank': 'True'}),
            'responsable_administrativo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'responsable_politico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sector_economico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['sujetos']