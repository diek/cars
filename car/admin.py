from django.contrib import admin

from .models import Car, Make

admin.site.register(Make)

admin.site.register(Car)
