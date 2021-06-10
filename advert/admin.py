from django.contrib import admin
from .models import Announcement, Category, AnnounCategory
# Register your models here.

class AnnounCategoryInline(admin.TabularInline):
    model = AnnounCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (AnnounCategoryInline,)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    inlines = (AnnounCategoryInline,)