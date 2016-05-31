from django.contrib import admin

from .models import Company, Contact, Process, Skill


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact)
admin.site.register(Process)
admin.site.register(Skill)
