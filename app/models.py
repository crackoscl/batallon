from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = RichTextField(default='aqui texto')
    fecha = models.DateField()
    link_evento = models.CharField(max_length=400)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        ordering = ['-nombre']


class Comuna(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE,related_name='comunas')
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre


class Clubes(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE)
    logo = models.URLField(max_length=400, default='logo')
    imagen_perfil = models.URLField(max_length=400 ,default='aqui imagen perfil')
    description = RichTextField(default='aqui texto')

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"

    def __str__(self) -> str:
        return self.nombre


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.nombre


class Peleador(models.Model):
    FEMENINO = 'F'
    MASCULINO = 'M'
    SEXO_CHOICES = [
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino')
    ]

    nombre = nombre = models.CharField(max_length=50)
    club = models.ForeignKey(Clubes, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    class Meta:
        verbose_name = "Peleador"
        verbose_name_plural = "Peleadores"

    def __str__(self) -> str:
        return f'nombre: {self.nombre}, club: {self.club}'


class Rating(models.Model):
    rank = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    peleador = models.ForeignKey(Peleador, on_delete=models.CASCADE)
    rating = models.FloatField()
    rd = models.FloatField()

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self) -> str:
        return f'{self.rank} {self.categoria}'


class Usuario(AbstractUser):
    apellido_paterno = models.CharField(
        max_length=50, null=True, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(
        max_length=50, null=True, verbose_name="Apellido Materno")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Rut: {self.username} - {self.apellido_materno} - {self.apellido_paterno}'

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
