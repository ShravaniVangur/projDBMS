from django.contrib import admin
from .models import police_station,crime_register,accused,witness,officer_record,victim

admin.site.register(police_station)
admin.site.register(crime_register)
admin.site.register(accused)
admin.site.register(witness)
admin.site.register(officer_record)
admin.site.register(victim)
