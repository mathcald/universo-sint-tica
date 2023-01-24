from django.urls import path
from grupo.views import index, imagem, cadastro

urlpatterns = [
        path('', index, name='index'),
        path('imagem/', imagem, name='imagem'),
        path('cadastro/', cadastro, name='cadastro')
]