from django.urls import path, include
from .views import MovieListView, MovieDetailView, favorite_movie, MovieCreateView, MovieUpdateView, MovieDeleteView
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)


app_name = 'movies'

urlpatterns = [
    #URLS Gerais
    path('', views.movie_list, name='movie_list'),
    path('api/', include(router.urls)),
    

        #DETALHES
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),

        #NOVO FILME
        path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
        path('add/', views.add_movie, name='add_movie'),    

        #DELETAR
    path('remove_movie/<int:movie_id>/', views.remove_movie, name='remove_movie'),

        #ATUALIZAR
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),

        #EDITAR
    path('<int:movie_id>/edit/', views.edit_movie, name='edit_movie'),

        #MARCAR COMO ASSISTIDO
    path('watched/<int:movie_pk>/', views.mark_watched, name='mark_watched'),

        #MARCAR COMO FAVORITO
    path('movie/<int:pk>/favorite/', views.favorite_movie, name='favorite_movie'),

    #URLS Login e Logout
    path('accounts/login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),


    #OUTRAS URLS
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
]
