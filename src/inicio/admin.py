from django.contrib import admin
from inicio.models import Squad

@admin.register(Squad)

# class InicioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'titulo', 'imagem')
#     list_display_links = ('id', 'titulo')
#     search_fields = ['titulo']
#     list_per_page = 10
#     list_filter = ['titulo']
#     list_editable = ['imagem']

class SquadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']
    list_per_page = 10
    list_filter = ['nome']
    list_editable = ['imagem']

