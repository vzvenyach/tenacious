# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Submission.is_public'
        db.delete_column(u'forms_submission', 'is_public')

        # Deleting field 'Survey.ends_at'
        db.delete_column(u'forms_survey', 'ends_at')

        # Deleting field 'Survey.allow_comments'
        db.delete_column(u'forms_survey', 'allow_comments')

        # Deleting field 'Survey.allow_voting'
        db.delete_column(u'forms_survey', 'allow_voting')

        # Deleting field 'Survey.starts_at'
        db.delete_column(u'forms_survey', 'starts_at')

        # Deleting field 'Survey.archive_policy'
        db.delete_column(u'forms_survey', 'archive_policy')

        # Deleting field 'Survey.moderate_submissions'
        db.delete_column(u'forms_survey', 'moderate_submissions')


        # Changing field 'Survey.survey_date'
        db.alter_column(u'forms_survey', 'survey_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True))

    def backwards(self, orm):
        # Adding field 'Submission.is_public'
        db.add_column(u'forms_submission', 'is_public',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Survey.ends_at'
        db.add_column(u'forms_survey', 'ends_at',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Survey.allow_comments'
        db.add_column(u'forms_survey', 'allow_comments',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Survey.allow_voting'
        db.add_column(u'forms_survey', 'allow_voting',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Survey.starts_at'
        db.add_column(u'forms_survey', 'starts_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Survey.archive_policy'
        db.add_column(u'forms_survey', 'archive_policy',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Survey.moderate_submissions'
        db.add_column(u'forms_survey', 'moderate_submissions',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Survey.survey_date'
        db.alter_column(u'forms_survey', 'survey_date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forms.answer': {
            'Meta': {'ordering': "('question',)", 'object_name': 'Answer'},
            'boolean_answer': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date_answer': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'float_answer': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integer_answer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.Question']"}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.Submission']"}),
            'text_answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'forms.question': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('fieldname', 'survey'),)", 'object_name': 'Question'},
            'answer_is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fieldname': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'help_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'map_icons': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'numeric_is_int': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'option_type': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'options': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'question_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'question_section'", 'null': 'True', 'to': u"orm['forms.Section']"}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['forms.Survey']"}),
            'use_as_filter': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'forms.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'survey'", 'to': u"orm['forms.Survey']"})
        },
        u'forms.submission': {
            'Meta': {'ordering': "('-submitted_at',)", 'object_name': 'Submission'},
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.Survey']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'forms.survey': {
            'Meta': {'ordering': "('-survey_date',)", 'unique_together': "(('survey_date', 'slug'),)", 'object_name': 'Survey'},
            'default_report': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports'", 'null': 'True', 'to': u"orm['forms.SurveyReport']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'has_script': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sections': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sections'", 'null': 'True', 'to': u"orm['forms.Section']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'survey_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thanks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'forms.surveyreport': {
            'Meta': {'ordering': "('title',)", 'unique_together': "(('survey', 'slug'),)", 'object_name': 'SurveyReport'},
            'display_individual_results': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'display_the_filters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_results_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_by_rating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'forms.surveyreportdisplay': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SurveyReportDisplay'},
            'aggregate_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'annotation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption_fields': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_type': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'fieldnames': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_map_answers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_center_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'map_center_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'map_zoom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.SurveyReport']"}),
            'x_axis_fieldname': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['forms']