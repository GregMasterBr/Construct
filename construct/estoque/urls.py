from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('excluir_produto/<str:id>/', views.excluir_produto, name='excluir_produto'),

]
