from django.contrib import admin
from polls.models import Poll, Choice

# we can replace the following line in order to edit the admin form for the polls.
#admin.site.register(Poll)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	"""Forma de la administracion para las encuestas """
#	fields = ['Fecha','Pregunta']
	fieldsets = [
		("Pregunta",				{'fields': 	['question']}),
		('Informacion de la fecha', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)