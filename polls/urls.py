from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagem/<int:pk>/', views.detalhes_postagem, name='detalhes_postagem'),
    path('categorias/<str:categoria_slug>/', views.postagens_por_categoria, name='postagens_por_categoria'),
    path('search/', views.search_results, name='search_results'),


    path('login/', views.login_blog, name="login"),
    path('logout/', views.logout_blog, name="logout"),


    path('categorias/', views.categorias, name='categorias'),
    path('salvar_categoria/', views.salvar_categoria, name='salvar_categoria'),
    path('editar_categoria/', views.editar_categoria, name='editar_categoria'),

    
]