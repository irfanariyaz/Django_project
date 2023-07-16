from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Classifields)
admin.site.register(Subcategory)
admin.site.register(Location)
admin.site.register(Category)


