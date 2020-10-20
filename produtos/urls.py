from django.urls import path
from produtos import views


urlpatterns = [
    path('lista/', views.lista_produtos, name='lista'),
    path('novo/', views.novo_produto, name='cadastrar_produto'),
    path('edita_produto/<int:id>/', views.edita_produto, name='editar_produto'),
    path('deleta_produto/<int:id>/', views.deleta_produto, name='deletar_produto'),
]
