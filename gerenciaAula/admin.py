from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['user', 'nome', 'nivel_usuario', 'eventual_doc', 'cod_discList', 'created']
    empty_value_display = 'Vazio'
    list_display_links = 'user', 'nivel_usuario'
    list_filter = 'user__is_active', 'user__is_superuser'
    fieldsets = ((
        ('Usuário', {
            'fields': ('user', 'nome', 'image', 'nivel_usuario'),
        })
    ),
        ('Disciplinas', {
            'fields': ('cod_disc',)
        }),
    )
    search_fields = 'user__username',
    
    def created(self, obj):
        return obj.created_at
    created.empty_value_display = '__/__/____'

    def cod_discList(self, obj):
        return [i.cod_disc for i in obj.cod_disc.all()]

# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aula)
admin.site.register(Disciplina)
admin.site.register(Habilidade)
admin.site.register(Turma)