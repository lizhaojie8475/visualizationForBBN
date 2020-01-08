from django.contrib import admin
from .models import userModel, nationalCity, traceRoute
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password', 'create_time', 'update_time')
    ordering = ('create_time',)
    search_fields = ('user_name',)

class cityAdmin(admin.ModelAdmin):
    list_display = ('countyName', 'center', 'status', 'probe', 'silhouetteScore')
    ordering = ('countyName',)
    search_fields = ('countyName',)

class traceRouteAdmin(admin.ModelAdmin):
    list_display = ('sourceIP', 'sourceCity', 'targetIP')
    search_fields = ('sourceIP',)

admin.register(userModel, userAdmin)
admin.register(nationalCity, cityAdmin)
admin.register(traceRoute, traceRouteAdmin)