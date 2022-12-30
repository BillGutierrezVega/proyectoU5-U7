from rest_framework import routers

from servicios.api import ServicesViewSet



router = routers.DefaultRouter(trailing_slash=False)

router.register('servicios/', ServicesViewSet, 'servicios')

urlpatterns = router.urls
 