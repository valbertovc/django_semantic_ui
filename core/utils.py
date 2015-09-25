# -*- coding: utf-8 -*-
from django.forms.utils import ErrorList
from django.utils.encoding import force_text
from django.utils.html import escape, format_html, format_html_join, html_safe
from django.utils.safestring import mark_safe


class SemanticIcons(object):
    '''
    Show semantic icons from passed value
    '''

    @staticmethod
    def as_boolean_icons(value):
        '''
        display icon for boolean value
        '''
        true_icon = 'check green'
        false_icon = 'remove red'
        html_icon = '<i class="{} icon"></i>'
        if value:
            return format_html(html_icon, mark_safe(true_icon))
        else:
            return format_html(html_icon, mark_safe(false_icon))


class SemanticErrorList(ErrorList):

    def __unicode__(self):
        return self.as_list()

    def as_error_message(self):
        if not self.data:
            return ''
        return format_html(
            u'<div class="{}"><i class="circular close icon"></i>{}</div>',
            u'ui error message',
            format_html_join('', u'<p>{}</p>', ((force_text(e),) for e in self))
        )

    def as_list(self):
        if not self.data:
            return ''
        return format_html(
            u'<div class="{}">{}</div>',
            u'ui list',
            format_html_join('', u'<div class="item">{}</div>', ((force_text(e),) for e in self))
        )

    
    def as_pointing_label(self, position='top'):
        """
        Options of position: top, left, right and bottom
        """
        if not self.data:
            return ''
        return format_html(
            u'<div class="{}"><i class="circle remove icon"></i>{}</div>',
            u'ui top pointing red label',
            format_html_join('', u'{}', ((force_text(e),) for e in self))
        )

    def __init__(self, initlist=None, error_class=None):
        super(ErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'error'
        else:
            self.error_class = '{}'.format(error_class)
