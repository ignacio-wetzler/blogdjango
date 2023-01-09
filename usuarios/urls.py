from django.urls import path
from . import views

urlpatterns = [
    path('alta/', views.alta_usuario, name= "alta"),
]