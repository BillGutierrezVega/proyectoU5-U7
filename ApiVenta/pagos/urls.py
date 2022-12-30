from rest_framework import routers

from pagos.api import PagosHechosViewSet, PagosExpiradosViewSet


router = routers.DefaultRouter()

router.register('api/pagosRealizados', PagosHechosViewSet, 'pagosHechos')
router.register('api/pagosExpirados', PagosExpiradosViewSet, 'pagosExpirados')

urlpatterns = router.urls

