from django.urls import path
from .views import order_create
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('create/'), order_create, name="order_create"),
]