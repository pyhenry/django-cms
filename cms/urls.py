from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^estoque', views.estoque, name='estoque'),
    url(r'^nova-venda', views.nova_venda, name='nova_venda'),
    url(r'^nova-nota', views.cad_notas, name='cad_notas'),
    url(r'^cadastrar-produtos', views.cad_novo_produto, name='cad_novo_produto'),
    url(r'^cadastrar-cliente', views.cad_novo_cliente, name='cad_novo_cliente'),
    url(r'^novo-usuario', views.cad_novo_usuario , name='cad_novo_usuario'),
    url(r'', views.cms, name='cms'),
]
