from django.contrib import admin
from .models import userModel, nationalCity, traceRoute
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('userName', 'password', 'createTime', 'updateTime')
    ordering = ('createTime',)
    search_fields = ('userName',)

class cityAdmin(admin.ModelAdmin):
    list_display = ('countyName', 'center', 'status', 'probe', 'silhouetteScore')
    ordering = ('countyName',)
    search_fields = ('countyName',)

class traceRouteAdmin(admin.ModelAdmin):
    list_display = ('sourceIP', 'sourceCity', 'targetIP')
    search_fields = ('sourceIP',)

admin.site.register(userModel, userAdmin)
admin.site.register(nationalCity, cityAdmin)
admin.site.register(traceRoute, traceRouteAdmin)