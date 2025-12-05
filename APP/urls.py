from rest_framework.routers import DefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'saladas', SaladaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = router.urls