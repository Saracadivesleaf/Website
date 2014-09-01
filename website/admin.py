from django.contrib import admin
from website.models import Navigation

# Register your models here.
class NavigationAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'parent_navigation',)

admin.site.register(Navigation, NavigationAdmin)
