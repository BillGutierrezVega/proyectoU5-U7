from rest_framework import routers

from servicios.api import ServicesViewSet



router = routers.DefaultRouter(trailing_slash=True)


router.register('api/servicios', ServicesViewSet, 'servicios')


urlpatterns = router.urls
 