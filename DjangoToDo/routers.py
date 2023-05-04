from rest_framework.routers import DefaultRouter

from ToDo.viewsets import UserGenericViewSet

router = DefaultRouter()
router.register('users', UserGenericViewSet, basename='users')
urlpatterns = router.urls