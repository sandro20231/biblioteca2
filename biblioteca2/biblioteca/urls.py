from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inserirautor/', views.inserirautor, name="inserirautor"),
    path('inserirlivro/', views.inserirlivro, name="inserirlivro"),
    path('login/', views.login, name="login"),
    path('listarautores/', views.listarautores, name="listarautores"),
    path('listarlivros/', views.listarlivros, name="listarlivros"),
    path('listarautores/<int:id>/', views.mostrarautor, name="mostrarautor"),
    path('listarlivros/<int:id>/', views.mostrarlivro, name="mostrarlivro"),
    path('listarautores/<int:id>/deletar',
         views.deletarautor, name="deletarautor"),
    path('listarlivros/<int:id>/deletar',
         views.deletarlivros, name="deletarlivros"),
    path('listarautores/<int:id>/alterar',
         views.alterarautor, name="alterarautor")
]
