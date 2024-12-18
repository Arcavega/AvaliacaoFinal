from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserBlog

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('nome','ano')

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(FormServicos)
class FormServicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'numero', 'servico', 'data', 'aceita')
    list_filter = ('servico', 'data', 'aceita')
    search_fields = ('nome', 'email', 'detalhes')
    ordering = ('-data',)

class UserBlogAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')}),
    )

admin.site.register(UserBlog, UserBlogAdmin)
