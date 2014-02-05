# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Paragraph.paraId'
        db.delete_column(u'wa_paragraph', 'paraId')


    def backwards(self, orm):
        # Adding field 'Paragraph.paraId'
        db.add_column(u'wa_paragraph', 'paraId',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    models = {
        u'wa.book': {
            'Meta': {'object_name': 'Book'},
            'aBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bookName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dBookDownloads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wa.Language']"}),
            'percentageAudioInvalid': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'percentageCompleteAudio': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'percentageCompleteDigi': ('django.db.models.fields.FloatField', [], {'default': '0'})
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