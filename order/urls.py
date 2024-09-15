from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("delivery_address", views.DeliveryAddressViewSet,
                basename='deliveryaddress')

urlpatterns = [
    path('', include(router.urls)),
    path("orders/", views.OrderView.as_view()),
    path("orders/card/", views.OrderWithCard.as_view()),
    path("orders/web-hook/", views.stripe_webhook),
    path("orders/successful-payment/", views.successful_payment),
]
