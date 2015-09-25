# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import DateTimeField
from django.forms.widgets import DateTimeInput
from django.conf import settings
from django.utils.html import format_html
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt


class SemanticMasked:
    class Media:
        js = (
            '/static/core/js/jquery.simple-dtpicker.js',
            '/static/core/js/jquery.mask.js'
        )

        css = {'all': ('/static/core/css/jquery.simple-dtpicker.css',)}


class SemanticDateTimeWidget(DateTimeInput, SemanticMasked):
    
    def render(self, name, value, attrs=None):
        field = super(SemanticDateTimeWidget, self).render(name, value, attrs)
        id_ = 'id_%s' % name
        div = '<div class="ui icon input">%s%s</div>%s'
        icon = '<i class="calendar icon"></i>'
        script = u"""
        <script>
            $(document).ready(function() {
                $('#%s').appendDtpicker({
                    "duration": '',
                    "locale": "br",
                    "closeOnSelected": true,
                    "dateFormat": "DD/MM/YYYY hh:mm"
                });

                $('.datepicker').on("blur", function (e) {
                    setTimeout(function () {
                        if (!context.is(':focus')) {
                            $(context).datepicker("hide");
                        }
                    }, 250); 
                });

            });
            $('#%s').mask('00/00/0000 00:00');
        </script>""" % (id_, id_)
        html = div % (field, icon, script) 
        return mark_safe(u'%s%s' % (html, script))


class DateTimeFieldSemantic(forms.DateTimeField):
    widget = SemanticDateTimeWidget()