from rest_framework import routers

from .api import UserViewSet



router = routers.DefaultRouter()

router.register('usuario/user', UserViewSet, 'user')

urlpatterns = router.urls
