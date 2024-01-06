from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

router = DefaultRouter()

router.register("user", UserModelViewSet)

urlpatterns = [] + router.urls