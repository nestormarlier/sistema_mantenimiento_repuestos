from django.contrib import admin
from .models import *

admin.site.site_header = 'Sistema de gestión de mantenimiento y repuestos.'
admin.site.index_title = 'Área de características'                 # default: 
admin.site.site_title = 'Sistema de gestión' # default: "Django site admin"
admin.site.register(Activo)
admin.site.register(Proveedor)
admin.site.register(OrdenTrabajo)
admin.site.register(MantenimientoPreventivo)
admin.site.register(HistorialMantenimiento)
admin.site.register(Repuesto)