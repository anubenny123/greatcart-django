from django.contrib import admin
from owner .models import *

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Order)
admin.site.register(Reviews)
