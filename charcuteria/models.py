from django.db import models

class Salazones(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class EmbutidoSeco(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class EmbutidoFresco(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class FuetSalch(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class EmbutidoIberico(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Sobrasada(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Jamon(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Legumbre(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Queso(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class QuesoImportacion(models.Model):
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class EmbutidoCorte(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Cocido(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Pate(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Especial(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Tostas(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre

class Conserva(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    pvp = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return self.nombre
