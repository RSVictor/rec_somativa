from django.db import models
from django.conf import settings


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Salada(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    salada_personalizada = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if self.personalizada:
            self.preco = 45.00
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Pedido(models.Model): 
    STATUS = ( ('andamento', 'Em andamento'), 
                ('producao', 'Em produção'), 
                ('entregue', 'Entregue'), 
                )
    criado_em = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        soma = 0
        for s in self.saladas.all():
            soma += s.preco
        self.total = soma
        self.save()

def __str__(self):
    return f"Pedido {self.id} - {self.usuario.username}"

class Avaliacoes(models.Model): 
    pedido = models.OneToOneField(to='Pedido', on_delete=models.CASCADE)
    nota = models.IntegerField(null=False, blank=False, default=0)
    comentario = models.CharField(max_length=100)

