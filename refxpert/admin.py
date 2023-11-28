from django.contrib import admin

# Register your models here.
from .models import  Tag, HouseApplication, LegalService, PropertyManagement, TenantForm, BlogPost



admin.site.register(Tag)
admin.site.register(HouseApplication)
admin.site.register(LegalService)
admin.site.register(PropertyManagement)
admin.site.register(TenantForm)
admin.site.register(BlogPost)