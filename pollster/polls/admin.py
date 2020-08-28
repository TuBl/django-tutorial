from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.site_index_title = "Welcome to the Pollster Admin area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    # howmany extra fields you want (beside the already populate ones)
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # first field is a name. None when you don't need one
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes':['collapse']
    }), ]  # this is a tuple, that is why we need the trailing comma in the end
    inlines = [ChoiceInLine]
# admin.site.register(Question)
# admin.site.register(Choice)


admin.site.register(Question, QuestionAdmin)
