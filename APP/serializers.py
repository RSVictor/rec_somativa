from rest_framework import serializers
from .models import Ingrediente, salada, Pedido

class Ingredienteserializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [ '__all_']

class SaladaSerializers(serializers.ModelSerializer):
    ingredientes = IngredienteSelializer(many=True, read_only=True)
    ingredientes_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingrediente.objects.all(),
        write_only=True 
    )

     class Meta:
        model = Salada
        fields = ['id', 'nome', 'ingredientes', 'ingredientes_ids', 'preco', 'personalizada']
        read_only_fields = ['preco']

def create(self, validated_data):
    ingredientes_ids = validated_data.pop('ingredientes_ids')
    salada = Salada.objects.create(**validated_data)
    salada.ingredientes.set(ingredientes_ids)
    salada.save()

    return salada


class PedidoSerializer(serializers.ModelsModelSerializer):
    saladas_ids = serializers.PrimaryKeyRelatedField( many=True, queryset=Salada.objects.all(), write_only=True )

        class Meta:
            model = Pedido
            fields = ['id', 'usuario', 'saladas', 'saladas_ids', 'status', 'total', 'criado_em']
            read_only_fields = ['total']

    def create(self, validated_data):
        saladas_ids = validated_data.pop('saladas_ids')
        pedido = Pedido.objects.create(**validated_data)
        pedido.saladas.set(saladas_ids)
        pedido.calcular_total()

        return pedido

    