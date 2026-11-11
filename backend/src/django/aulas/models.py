from django.db import models

# Create your models here.

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)
    apellido = models.CharField(max_length=128, null=False, blank=False)
    mostrar = models.CharField(max_length=256, null=False, blank=False)

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)
    cant_alumnos = models.IntegerField(null=False, default=5)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, db_column='id_carrera')
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, db_column='id_profesor')

class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128, null=False, blank=False)
    ubicacion = models.CharField(max_length=128, null=False, blank=False)
    cant_proyector = models.IntegerField(blank=True, default=0)
    aforo = models.IntegerField(blank=True, default=0)
    es_climatizada = models.BooleanField(default=False)


class reserva_aula(models.Model):
    id = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE, db_column='id_aula')
    fh_desde = models.DateTimeField(null=False, blank=False)
    fh_hasta = models.DateTimeField(null=False, blank=False)
    observacion = models.CharField(max_length=256)

class horario_materia(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, db_column='id_materia')
    id_reserva = models.ForeignKey(reserva_aula, on_delete=models.CASCADE, db_column='id_reserva')
    fh_desde = models.DateTimeField(null=False, blank=False)
    fh_hasta = models.DateTimeField(null=False, blank=False)