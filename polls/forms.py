# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django import forms
from polls.models import Question, Choice
from core.formfields import DateTimeFieldSemantic
from django.utils.translation import ugettext_lazy as _


class ChoiceForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Choice
        exclude = ()
        widgets = {
            'question': forms.Select(attrs={'class': 'ui fluid dropdown'}),
        }


class QuestionForm(ModelForm):
    pub_date = DateTimeFieldSemantic(label=_('Pub date'), localize=True, help_text=u'dd/mm/yyyy hh:mm')

    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = Question
        exclude = ()