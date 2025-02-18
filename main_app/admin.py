from django.contrib import admin
from main_app.models import Resort, Reservation, Review

# Register your models here.
admin.site.register(Resort)
admin.site.register(Reservation)
admin.site.register(Review)