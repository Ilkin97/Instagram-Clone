from django.contrib import admin
from .models import CustomUser


admin.site.site_header = "Django Blog Admin"
admin.site.site_title = "Django Blog Admin Area"
admin.site.index_title = "Welcome to the Django Blog Admin Area"

admin.site.register(CustomUser)