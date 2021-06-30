
from rest_framework import serializers
from movies.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Actor
        fields = ('name', 'age', 'description', 'image')


class GenreSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Genre
        fields = ('name', 'description', 'url')


class MovieShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='account.email')

    class Meta:
        model = Like
        fields = ('movie', 'like', 'user',)


class MovieSerializer(serializers.ModelSerializer):

    # category = CategorySerializer(many=False, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    poster = MovieShotSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

        # fields = (
        # 'title', 'description', 'poster', 'year', 'country', 'directors', 'actors', 'genres', 'world_premiere',
        # 'budget', 'fees_in_world ', 'category', 'url')

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     # images_data = request.FILES
    #     movie = Movie.objects.create(**validated_data)
    #     # print(images_data.getlist('images'))
    #     # for image in images_data.getlist('images'):
    #     #     MovieShots.objects.create(product=movie, image=image)
    #     return movie

    def to_representation(self, instance):
        representation = super(MovieSerializer, self).to_representation(instance)
        action = self.context.get('action')
        likes = LikeSerializer(instance.likes.filter(like=True), many=True).data
        if action == 'list':
            representation['likes'] = {'like': likes}
            representation['likes'] = instance.likes.filter(like=True).count()
        if action == 'retrieve':
            representation['likes'] = likes
        return representation

    # def validate(self, attrs):
    #     return super().validate(attrs)


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Basket
        fields = ('movie', 'basket', 'user',)


class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Favorite
        fields = ('movie', 'favorite', 'user',)



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('name', 'movie', 'text', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.profile_customer
        review = Reviews.objects.create(user=user, **validated_data)
        return review

    def to_representation(self, instance):
        representation = super(ReviewSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        return representation