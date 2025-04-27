from rest_framework import serializers
from .models import Category, Idea



class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'
        # fields = ['id', 'title', 'body', 'category']


class CategorySerializer(serializers.ModelSerializer):
    ideas = IdeaSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'prompt': {'required': False, 'allow_blank': True},
        }
        # fields = ['id', 'name', 'user']