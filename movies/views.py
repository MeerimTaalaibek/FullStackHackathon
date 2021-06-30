
from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework import permissions
from movies.permissions import IsOwnerOrReadOnly
from movies import serializer
from movies.models import *

from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from movies.serializer import CategorySerializer, ReviewSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [AllowAny, ]

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializer.MovieSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('title', 'price', 'country')
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(id__icontains=search) | Q(price__icontains=search))
        return queryset

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializer.MovieSerializer


class BasketListView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = serializer.BasketSerializer


class BasketCreateView(generics.CreateAPIView):
    serializer_class = serializer.BasketSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BasketDeleteView(generics.DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = serializer.BasketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializer.LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    serializer_class = serializer.LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = serializer.LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class FavoritesListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = serializer.FavoritesSerializer


class FavoritesCreateView(generics.CreateAPIView):
    serializer_class = serializer.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoritesDeleteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = serializer.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)



class ReviewViewSet( viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


