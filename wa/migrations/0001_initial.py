# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'wa_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('languages_known', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phoneNo', self.gf('django.db.models.fields.BigIntegerField')(max_length=15)),
            ('loginTimes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'wa', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name(u'wa_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'wa.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name(u'wa_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'wa.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])

        # Adding model 'Language'
        db.create_table(u'wa_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('langName', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'wa', ['Language'])

        # Adding model 'Book'
        db.create_table(u'wa_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lang', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.Language'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bookName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('percentageCompleteAudio', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('percentageCompleteDigi', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('percentageAudioInvalid', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('dBookDownloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('aBookDownloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('numberOfChunks', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'wa', ['Book'])

        # Adding model 'Paragraph'
        db.create_table(u'wa_paragraph', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.Book'])),
            ('audioAssignedTo', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='audioAssignedTo', null=True, blank=True, to=orm['wa.CustomUser'])),
            ('audioReadBy', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='audioReadBy', null=True, blank=True, to=orm['wa.CustomUser'])),
            ('isRecording', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('digiAssignedTo', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='digiAssignedTo', null=True, blank=True, to=orm['wa.CustomUser'])),
            ('digiBy', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='digiBy', null=True, blank=True, to=orm['wa.CustomUser'])),
            ('isDigitizing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isChapter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validAudioVersionNumber', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('upVotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('downVotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'wa', ['Paragraph'])

        # Adding model 'UserHistory'
        db.create_table(u'wa_userhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.CustomUser'])),
            ('loginTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('logoutTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 21, 0, 0))),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('paragraph', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['wa.Paragraph'], null=True, blank=True)),
            ('vote', self.gf('django.db.models.fields.CharField')(default=None, max_length=2, null=True, blank=True)),
            ('audioVersion', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('uploadedBook', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['wa.Book'], null=True, blank=True)),
        ))
        db.send_create_signal(u'wa', ['UserHistory'])

        # Adding model 'Document'
        db.create_table(u'wa_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'wa', ['Document'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'wa_customuser')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name(u'wa_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name(u'wa_customuser_user_permissions'))

        # Deleting model 'Language'
        db.delete_table(u'wa_language')

        # Deleting model 'Book'
        db.delete_table(u'wa_book')

        # Deleting model 'Paragraph'
        db.delete_table(u'wa_paragraph')

        # Deleting model 'UserHistory'
        db.delete_table(u'wa_userhistory')

        # Deleting model 'Document'
        db.delete_table(u'wa_document')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'codename',)", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wa.book': {
            'Meta': {'object_name': 'Book'},
            'aBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bookName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Language']"}),
            'numberOfChunks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'percentageAudioInvalid': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'percentageCompleteAudio': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'percentageCompleteDigi': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'wa.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages_known': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'loginTimes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phoneNo': ('django.db.models.fields.BigIntegerField', [], {'max_length': '15'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'wa.document': {
            'Meta': {'object_name': 'Document'},
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wa.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'langName': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'wa.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'audioAssignedTo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'audioAssignedTo'", 'null': 'True', 'blank': 'True', 'to': u"orm['wa.CustomUser']"}),
            'audioReadBy': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'audioReadBy'", 'null': 'True', 'blank': 'True', 'to': u"orm['wa.CustomUser']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Book']"}),
            'digiAssignedTo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'digiAssignedTo'", 'null': 'True', 'blank': 'True', 'to': u"orm['wa.CustomUser']"}),
            'digiBy': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'digiBy'", 'null': 'True', 'blank': 'True', 'to': u"orm['wa.CustomUser']"}),
            'downVotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isChapter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isDigitizing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isRecording': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'upVotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'validAudioVersionNumber': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'wa.userhistory': {
            'Meta': {'object_name': 'UserHistory'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'audioVersion': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loginTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'logoutTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 21, 0, 0)'}),
            'paragraph': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['wa.Paragraph']", 'null': 'True', 'blank': 'True'}),
            'uploadedBook': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['wa.Book']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.CustomUser']"}),
            'vote': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wa']