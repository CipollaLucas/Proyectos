from django.urls import path
from compras import views


urlpatterns = [path("", views.index, name="index")]
