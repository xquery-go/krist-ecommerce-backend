from django.urls import path
from . import views


urlpatterns = [
    path('accounts/register/', views.AccountView.as_view()),
    path('accounts/login/', views.AccountLoginView.as_view()),
]
