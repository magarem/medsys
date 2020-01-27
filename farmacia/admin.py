from django.contrib import admin

from .models import Remedio

class RemedioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'unidade', 'validade', 'obs')

admin.site.register(Remedio, RemedioAdmin)
