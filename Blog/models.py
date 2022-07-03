from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.TextField()
    fecha = models.DateField()
    autor = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo + "|" + self.autor

opciones_consultas = [
    [0, "consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"Felicitaciones, la página está muy buena"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre