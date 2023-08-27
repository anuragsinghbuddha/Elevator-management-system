from django.contrib import admin

# Register your models here.
from .models import Elevator, Request

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'operational', 'current_floor', 'moving_up', 'doors_open')
    list_filter = ('operational', 'moving_up', 'doors_open')
    search_fields = ('id', 'current_floor')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'elevator', 'floor', 'direction', 'completed')
    list_filter = ('elevator', 'direction', 'completed')
    search_fields = ('id', 'elevator__id', 'floor')

