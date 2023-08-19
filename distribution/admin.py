from django.contrib import admin
from distribution.models import Distribution


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status', 'message', )
    list_filter = ('status', )
    search_fields = ('time', 'frequency', 'status',)
