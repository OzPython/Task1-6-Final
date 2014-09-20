from django.contrib import admin
from polls.models import Poll,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently') #Creates 3 Columes For Data Output
    list_filter = ['pub_date'] # Adds A Filter sidebar sorting the pub_date field
    search_fields = ['question']
    list_per_page=200 #Set No. Of Items Per Page

admin.site.register(Poll, PollAdmin)

