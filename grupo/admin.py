from django.contrib import admin
from grupo.models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codinome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)



admin.site.register(Pessoa, ListandoPessoas)

