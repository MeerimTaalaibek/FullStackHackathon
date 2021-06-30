from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
    path('movies', MovieListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('categories/<str:pk>/', CategoryDetailView.as_view()),
    path('favorites/', FavoritesListView.as_view()),
    path('favorites/create/', FavoritesCreateView.as_view()),
    path('favorites/<int:pk>/delete/',FavoritesDeleteView.as_view()),

    path('basket/', BasketListView.as_view()),
    path('basket/create/', BasketCreateView.as_view()),
    path('basket/<int:pk>/delete/', BasketDeleteView.as_view()),

    path('likes/', LikeListView.as_view()),
    path('like/create/', LikeCreateView.as_view()),
    path('like/<int:pk>/delete/', views.LikeDeleteView.as_view()),




]
