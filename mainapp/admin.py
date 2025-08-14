from django.contrib import admin

# Register your models here.
from .models import HomeBanner

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)