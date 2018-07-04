from django.db import models

# Create your models here.
class Noticia(models.Model):
	informacion = models.CharField("Informacion", max_length=780)
	titulo = models.CharFIeld("Titulo", max_length=120)
	fecha = models.DateTimeField(auto_now=False, auto_now_add=False)

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"

	def __init__(self):
		return "{} {} {}".format(self.informacion, self.titulo, self.fecha)

class Comentario(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
	comentario = models.CharField("Comentario", max_length=240)

	class Meta:
		verbose_name = "Comentario"
		verbose_name_plural = "Comentarios"

	def __init__(self):
		return "{} {} {}".format(self.usuario, self.noticia, self.comentario)

