# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'forms_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('tease', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thanks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('moderate_submissions', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_voting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archive_policy', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('starts_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('survey_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ends_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('has_script', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sections', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sections', null=True, to=orm['forms.Section'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('default_report', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reports', null=True, to=orm['forms.SurveyReport'])),
        ))
        db.send_create_signal(u'forms', ['Survey'])

        # Adding unique constraint on 'Survey', fields ['survey_date', 'slug']
        db.create_unique(u'forms_survey', ['survey_date', 'slug'])

        # Adding model 'Question'
        db.create_table(u'forms_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['forms.Survey'])),
            ('fieldname', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('question_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.TextField')()),
            ('help_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='question_section', null=True, to=orm['forms.Section'])),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('option_type', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('numeric_is_int', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('options', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('map_icons', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('answer_is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('use_as_filter', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'forms', ['Question'])

        # Adding unique constraint on 'Question', fields ['fieldname', 'survey']
        db.create_unique(u'forms_question', ['fieldname', 'survey_id'])

        # Adding model 'Section'
        db.create_table(u'forms_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='survey', to=orm['forms.Survey'])),
        ))
        db.send_create_signal(u'forms', ['Section'])

        # Adding model 'Submission'
        db.create_table(u'forms_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.Survey'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('submitted_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'forms', ['Submission'])

        # Adding model 'Answer'
        db.create_table(u'forms_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.Submission'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.Question'])),
            ('text_answer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_answer', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('integer_answer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('float_answer', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('boolean_answer', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'forms', ['Answer'])

        # Adding model 'SurveyReport'
        db.create_table(u'forms_surveyreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.Survey'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort_by_rating', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display_the_filters', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('limit_results_to', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display_individual_results', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'forms', ['SurveyReport'])

        # Adding unique constraint on 'SurveyReport', fields ['survey', 'slug']
        db.create_unique(u'forms_surveyreport', ['survey_id', 'slug'])

        # Adding model 'SurveyReportDisplay'
        db.create_table(u'forms_surveyreportdisplay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forms.SurveyReport'])),
            ('display_type', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('aggregate_type', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('fieldnames', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('x_axis_fieldname', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('annotation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('limit_map_answers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_center_latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('map_center_longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('map_zoom', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('caption_fields', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'forms', ['SurveyReportDisplay'])


    def backwards(self, orm):
        # Removing unique constraint on 'SurveyReport', fields ['survey', 'slug']
        db.delete_unique(u'forms_surveyreport', ['survey_id', 'slug'])

        # Removing unique constraint on 'Question', fields ['fieldname', 'survey']
        db.delete_unique(u'forms_question', ['fieldname', 'survey_id'])

        # Removing unique constraint on 'Survey', fields ['survey_date', 'slug']
        db.delete_unique(u'forms_survey', ['survey_date', 'slug'])

        # Deleting model 'Survey'
        db.delete_table(u'forms_survey')

        # Deleting model 'Question'
        db.delete_table(u'forms_question')

        # Deleting model 'Section'
        db.delete_table(u'forms_section')

        # Deleting model 'Submission'
        db.delete_table(u'forms_submission')

        # Deleting model 'Answer'
        db.delete_table(u'forms_answer')

        # Deleting model 'SurveyReport'
        db.delete_table(u'forms_surveyreport')

        # Deleting model 'SurveyReportDisplay'
        db.delete_table(u'forms_surveyreportdisplay')


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
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forms.Survey']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'forms.survey': {
            'Meta': {'ordering': "('-starts_at',)", 'unique_together': "(('survey_date', 'slug'),)", 'object_name': 'Survey'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_voting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'archive_policy': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'default_report': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports'", 'null': 'True', 'to': u"orm['forms.SurveyReport']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ends_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'has_script': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderate_submissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sections': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sections'", 'null': 'True', 'to': u"orm['forms.Section']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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