from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('contato/', views.cadastrar, name='cadastrar'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('administrador/', views.administrador, name='administrador'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('aceitar/<int:id>/', views.aceitar_servico, name='aceitar'),
    path('recusar/<int:id>/', views.recusar_servico, name='recusar'),
]
