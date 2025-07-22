from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'user', 'phone', 'created_at')  # отображаемые столбцы
    list_filter = ('date', 'user')  # фильтр по дате и автору
    search_fields = ('title', 'phone', 'comment')  # поиск по этим полям
    ordering = ('date', 'time')  # сортировка по умолчанию
