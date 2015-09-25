# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Choice', 'verbose_name_plural': 'Choices'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='accepted',
            field=models.BooleanField(default=True, verbose_name='Accepted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='attachment',
            field=models.FileField(default='', upload_to=b'questions', verbose_name='Attachment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='Choice text'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Votes'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='Question text'),
        ),
    ]
