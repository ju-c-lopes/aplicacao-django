from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['nome', 'nivel_usuario', 'eventual_doc', 'created']
    empty_value_display = 'Vazio'
    list_display_links = 'user', 'nivel_usuario'
    list_filter = 'user__is_active', 'user__is_superuser'
    fields = 'user', ('nivel_usuario',), 'image'
    search_fields = 'user__username',
    
    def created(self, obj):
        return obj.created_at
    created.empty_value_display = '__/__/____'

# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aula)
admin.site.register(Disciplina)
admin.site.register(Habilidade)
admin.site.register(Turma)