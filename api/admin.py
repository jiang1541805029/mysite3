from django.contrib import admin
from .models import Type, Jingdian

# Register your models here.
@admin.register(Type)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type_name')

@admin.register(Jingdian)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('i_d', 'name', 'label', 'address', 'open_time')