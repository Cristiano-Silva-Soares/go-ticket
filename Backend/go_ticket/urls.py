from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tickets.viewsets import TicketTypeViewSet, VisitSlotViewSet
from sales.viewsets import SaleViewSet
from users.viewsets import UserViewSet


router = DefaultRouter()

router.register(r'tickets', TicketTypeViewSet)
router.register(r'slots', VisitSlotViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]