# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'wa_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phoneNo', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('languages', self.gf('separatedvaluesfield.models.SeparatedValuesField')(max_length=254)),
            ('loginTimes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'wa', ['User'])

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
            ('percentageCompleteAudio', self.gf('django.db.models.fields.FloatField')()),
            ('percentageCompleteDigi', self.gf('django.db.models.fields.FloatField')()),
            ('percentageAudioInvalid', self.gf('django.db.models.fields.FloatField')()),
            ('dBookDownloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('aBookDownloads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'wa', ['Book'])

        # Adding model 'Paragraph'
        db.create_table(u'wa_paragraph', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.Book'])),
            ('paraId', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('audioAssignedTo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='audioAssignedTo', to=orm['wa.User'])),
            ('audioReadBy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='audioReadBy', to=orm['wa.User'])),
            ('isRecording', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('digiAssignedTo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='digiAssignedTo', to=orm['wa.User'])),
            ('digiBy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='digiBy', to=orm['wa.User'])),
            ('isDigitizing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isChapter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('validAudioVersionNumber', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('upVotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('downVotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'wa', ['Paragraph'])

        # Adding model 'UserHistory'
        db.create_table(u'wa_userhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.User'])),
            ('loginTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('logoutTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('paragraph', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wa.Paragraph'])),
            ('vote', self.gf('django.db.models.fields.CharField')(default=None, max_length=2)),
            ('audioVersion', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'wa', ['UserHistory'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'wa_user')

        # Deleting model 'Language'
        db.delete_table(u'wa_language')

        # Deleting model 'Book'
        db.delete_table(u'wa_book')

        # Deleting model 'Paragraph'
        db.delete_table(u'wa_paragraph')

        # Deleting model 'UserHistory'
        db.delete_table(u'wa_userhistory')


    models = {
        u'wa.book': {
            'Meta': {'object_name': 'Book'},
            'aBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bookName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Language']"}),
            'percentageAudioInvalid': ('django.db.models.fields.FloatField', [], {}),
            'percentageCompleteAudio': ('django.db.models.fields.FloatField', [], {}),
            'percentageCompleteDigi': ('django.db.models.fields.FloatField', [], {})
        },
        u'wa.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'langName': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'wa.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'audioAssignedTo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'audioAssignedTo'", 'to': u"orm['wa.User']"}),
            'audioReadBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'audioReadBy'", 'to': u"orm['wa.User']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Book']"}),
            'digiAssignedTo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'digiAssignedTo'", 'to': u"orm['wa.User']"}),
            'digiBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'digiBy'", 'to': u"orm['wa.User']"}),
            'downVotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isChapter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isDigitizing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isRecording': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paraId': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'upVotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'validAudioVersionNumber': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'wa.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('separatedvaluesfield.models.SeparatedValuesField', [], {'max_length': '254'}),
            'loginTimes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phoneNo': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.EmailField', [], {'max_length': '254'})
        },
        u'wa.userhistory': {
            'Meta': {'object_name': 'UserHistory'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'audioVersion': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loginTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'logoutTime': ('django.db.models.fields.DateTimeField', [], {}),
            'paragraph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Paragraph']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.User']"}),
            'vote': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '2'})
        }
    }

    complete_apps = ['wa']