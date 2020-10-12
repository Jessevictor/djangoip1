from django.contrib import admin
from Photos.models import gallery, Location, Category

# Register your models here.
admin.site.register(gallery)
admin.site.register(Location)
admin.site.register(Category)

