from django.shortcuts import render
 from rest_framework import viewsets, permissions
from .models import Ingrediente, Salada, Pedido, Avaliacao from .serializers import * from rest_framework.permissions import IsAuthenticated


class RegistrarUsuarioView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

class IngredienteViewSet(viewsets.ModelViewSet): 
    queryset = Ingrediente.objects.all() 
    serializer_class = IngredienteSerializer

class SaladaViewSet(viewsets.ModelViewSet): 
    queryset = Salada.objects.all() 
    serializer_class = SaladaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated] 
     queryset = Pedido.objects.all() 
     serializer_class = PedidoSerializer

    def get_queryset(self):
     user = self.request.user

    if user.groups.filter(name='FUNCIONARIO').exists():
        return Pedido.objects.all()  
    return Pedido.objects.filter(usuario=user) 

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all() 
    serializer_class = AvaliacaoSerializer