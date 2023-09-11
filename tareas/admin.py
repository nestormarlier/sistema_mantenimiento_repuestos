from django.contrib import admin
from .models import *

admin.site.register(Activo)
admin.site.register(Proveedor)
admin.site.register(OrdenTrabajo)
admin.site.register(MantenimientoPreventivo)
admin.site.register(HistorialMantenimiento)
admin.site.register(Repuesto)