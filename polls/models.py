# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(verbose_name=_(u'Question text'), max_length=200)
    pub_date = models.DateTimeField(verbose_name=_(u'Date published'))
    description = models.TextField(verbose_name=_(u'Description'))
    accepted = models.BooleanField(verbose_name=_('Accepted'))

    class Meta:
        verbose_name = _(u'Question')
        verbose_name_plural = _(u'Questions')

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('question_detail', args=[str(self.id)])

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(verbose_name=_(u'Choice text'), max_length=200)
    votes = models.IntegerField(verbose_name=_(u'Votes'), default=0)

    class Meta:
        verbose_name = _(u'Choice')
        verbose_name_plural = _(u'Choices')

    def __str__(self):
        return self.choice_text
