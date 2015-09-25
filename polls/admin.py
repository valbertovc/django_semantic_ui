from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Choice, Question
from polls.forms import QuestionForm, ChoiceForm
from core.utils import SemanticIcons
from django.utils.translation import ugettext_lazy as _


class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    actions = None
    list_display_links = None
    list_display = ('get_action_icons', 'question', 'choice_text', 'votes')
    form = ChoiceForm

    def get_action_icons(self, obj):
        '''
        Add action icons at admin list
        '''
        from django.core import urlresolvers
        change_url = urlresolvers.reverse('admin:polls_choice_change', args=(obj.id,))
        return mark_safe('<a href="{}"><i class="pencil yellow icon"></i></a>'.format(change_url))
    get_action_icons.short_description = u''


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('get_action_icons', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    actions = None
    list_display_links = None
    list_per_page = 10
    form = QuestionForm
    date_hierarchy = 'pub_date'
    
    fieldsets = (
        (None, { 'fields': ('question_text', 'pub_date')}),
        ('Advanced', { 'fields': ('description', 'accepted')}),
    )

    def get_action_icons(self, obj):
        from django.core import urlresolvers
        change_url = urlresolvers.reverse('admin:polls_question_change', args=(obj.id,))
        return mark_safe('<a href="{}"><i class="pencil yellow icon"></i></a>'.format(change_url))
    get_action_icons.short_description = u''

    def was_published_recently(self, obj):
        return SemanticIcons.as_boolean_icons(obj.was_published_recently())
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.short_description = _('Published recently?')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
