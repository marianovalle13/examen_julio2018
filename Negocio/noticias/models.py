from django.db import models
from django.conf import settings 
# Create your models here.

class Noticia(models.Model):
	informacion = models.CharField("Informacion",max_length=10000)
	titulo = models.CharField("Titulo", max_length=80)
	fecha = models.DateField(auto_now=False, auto_now_add=False)
 
	class Meta:
		verbose_name = "Nota"
		verbose_name_plural = "Notas"

	def __init__(self):
		return '{}{}{}'.format(self.titulo, self.informacion, self.fecha)


class Comentario(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
	comentario = models.CharField("Comentario", max_length=240)

	class Meta:
		verbose_name = "Comentario"
		verbose_name_plural = "Comentarios"

	def __init__(self):
		return '{}{}{}'.format(self.usuario,self.noticia,self.comentario)