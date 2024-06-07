from django.contrib import admin
from .models import Čtenář, Půjčka, Knihovna, Knihovník, Rezervace

admin.site.register(Čtenář)
admin.site.register(Půjčka)
admin.site.register(Knihovna)
admin.site.register(Knihovník)
admin.site.register(Rezervace)