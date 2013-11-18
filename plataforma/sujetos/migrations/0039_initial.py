# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'sujetos_persona', (
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('cedula', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(default='F', max_length=1)),
            ('numero_telefono', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('correo_electronico', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('indigena', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('discapacidad', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('especifique', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('condicion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('saberes', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'sujetos', ['Persona'])

        # Adding M2M table for field proyecto on 'Persona'
        m2m_table_name = db.shorten_name(u'sujetos_persona_proyecto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('persona', models.ForeignKey(orm[u'sujetos.persona'], null=False)),
            ('proyecto', models.ForeignKey(orm[u'sujetos.proyecto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['persona_id', 'proyecto_id'])

        # Adding model 'Proyecto'
        db.create_table(u'sujetos_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero_proyecto', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('parroquia', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('comunidades', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('consejos_comunales', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('horas_dictadas_fecha', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('horas_por_ejecutar', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('horas_contratadas', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('horas_proyectadas', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('monto_inversion', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_arranque', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('estatus', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('responsable_politico', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('responsable_administrativo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipo_proyecto', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sector_economico', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dimensiones_formativas', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'sujetos', ['Proyecto'])

        # Adding model 'Estado'
        db.create_table(u'sujetos_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_estado', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'sujetos', ['Estado'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'sujetos_persona')

        # Removing M2M table for field proyecto on 'Persona'
        db.delete_table(db.shorten_name(u'sujetos_persona_proyecto'))

        # Deleting model 'Proyecto'
        db.delete_table(u'sujetos_proyecto')

        # Deleting model 'Estado'
        db.delete_table(u'sujetos_estado')


    models = {
        u'sujetos.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_estado': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
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