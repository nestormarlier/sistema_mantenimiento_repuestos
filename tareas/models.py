from django.contrib.auth.models import User
from django.db import models

class Activo(models.Model):
    ESTADOS_ACTIVO = (
        ('func','Funcionamiento'),
        ('mant','Mantenimiento'),
        ('des', 'Desechado')
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=50,choices= ESTADOS_ACTIVO)
    ubicacion = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self) -> str:
        return self.nombre_empresa + '-' + self.contacto

    class Meta:
        verbose_name_plural = 'Proveedores'

class OrdenTrabajo(models.Model):
    ORDEN_PRIORIDAD = (
        ('1', 'Uno'),
        ('2', 'Dos'),
        ('3', 'Tres'),
        ('4', 'Cuatro'),
        ('5', 'Cinco')
    )
    ESTADO_ORDEN = (
        ('PEND', 'Pendiente'),
        ('PROC', 'En proceso'),
        ('COM', 'Completada')
    )
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    descripcion_orden = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(max_length=50, choices=ORDEN_PRIORIDAD)
    estado_orden = models.CharField(max_length=50, choices=ESTADO_ORDEN)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Orden: '+ str(self.id) + ' - ' + str(self.activo) + ' - ' + 'Prioridad: '+ str(self.prioridad)

    class Meta:
        verbose_name_plural = 'Ordenes de trabajo'

class MantenimientoPreventivo(models.Model):
    FRECUENCIA_MANT = (
        ('DIA', 'Diariamente'),
        ('SEM', 'Semanal'),
        ('MEN', 'Mensual'),
        ('TRI', 'Trimestral'),
        ('ANU', 'Anual')
    )
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    descripcion_mantenimiento = models.TextField()
    fecha_programada = models.DateField()
    frecuencia = models.CharField(max_length=50, choices=FRECUENCIA_MANT)

    def __str__(self) -> str:
        return str(self.activo) + ' - ' + self.descripcion_mantenimiento + ' - ' + 'Fecha programada: ' + str(self.fecha_programada.strftime('%d/%m/%Y'))   

class HistorialMantenimiento(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, null=True, blank=True)
    mantenimiento_preventivo = models.ForeignKey(MantenimientoPreventivo, on_delete=models.CASCADE, null=True, blank=True)
    fecha_mantenimiento = models.DateTimeField()
    descripcion_mantenimiento_realizado = models.TextField()
    costo_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2)
    responsable_mantenimiento = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.orden_trabajo) + ' - '+ str(self.mantenimiento_preventivo) + ' - ' + str(self.fecha_mantenimiento.strftime('%d/%m/%Y'))

class Repuesto(models.Model):
    nombre_repuesto = models.CharField(max_length=100)
    descripcion_repuesto = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio $ Arg.')
    cantidad_stock = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.nombre_repuesto + ' - '+ 'Proveedor:'+ str(self.proveedor) + ' - Canitidad: ' + str(self.cantidad_stock)