from rest_framework.routers import DefaultRouter

from .views import UserManagement

router = DefaultRouter()
router.register('', viewset=UserManagement, basename='users')  # ModelViewSet
# router.register('/logout', viewset=UserLogout, basename='logout')  # ModelViewSet
urlpatterns = router.urls
