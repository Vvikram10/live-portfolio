from django.contrib import admin
from.models import Certificate, Project,Skill,Contact
# Register your models here.

admin.site.register([Project,Skill,Contact])
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'category', 'date')
    list_filter = ('category', 'issuer')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
