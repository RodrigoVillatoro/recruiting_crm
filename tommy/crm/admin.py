from django.contrib import admin

from .models import Company, Contact, Job, Skill


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact)
admin.site.register(Job)
admin.site.register(Skill)
