from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Type Racer"
admin.site.site_title="Type Racer"


class UserAdmin(admin.ModelAdmin):
    list_filter=['date_joined','is_superuser','last_login']
    list_per_page=10
    list_display=['phone','firstname','lastname','is_superuser','is_staff','date_joined','is_active','last_login']
    fieldsets=[("User Information",{'fields':('phone','firstname','lastname')}),
                ("Permissions",{'fields':('is_superuser','is_staff','is_active')}),
                ('Extras',{'fields':('last_login','date_joined')})]
    readonly_fields=['is_superuser','is_staff','is_active','date_joined','last_login']

class QuoteAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display=["id",'text','difficulty']

class RankAdmin(admin.ModelAdmin):
    list_per_page=10
    list_display=["id",'user','quote','score','created_at','updated_at']
    list_filter=['created_at','updated_at']
    # readonly_fields=['score']




admin.site.register(Quote,QuoteAdmin)
admin.site.register(Customuser,UserAdmin)
admin.site.register(Rank,RankAdmin)