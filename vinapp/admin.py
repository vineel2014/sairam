from django.contrib import admin
from vinapp.models import Category,Page,UserProfile
# Register your models here.

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)

admin.site.site_title = 'Vineel site admin'
admin.site.site_header = 'Vineel Administration'

