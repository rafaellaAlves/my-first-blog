from django.db import models
from django.utils import timezone


class Post(models.Model):#define o modelo(objeto) com nome de 'Post'/com isso o Django sabe que deve ser salvo no banco
	#definindo as propriedade
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#determina um link para ouro modelo
	title = models.CharField(max_length=200)#numero de carcteres limitados
	text = models.TextField()#tipo de variavel de texto sem numero delimitado
	created_date = models.DateTimeField(default=timezone.now)#data e hora
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):#metodo inicializado para este objeto
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	# Create your models here.
