from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ToDoAction


class UserSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ToDoActionSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoAction
        fields = ('id', 'title', 'description')



class ToDoActionAddSerialize(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = ToDoAction
        fields = ('title', 'description', 'user')

    # def create(self, validated_data):
    #     user = User.objects.get(username=validated_data['user'])
    #     validated_data['user'] = user
    #     toDoAction = ToDoAction.objects.create(**validated_data)
    #
    #     return toDoAction


class ToDoActionDelSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoAction
        fields = ('id', 'title')
#
#
# class ToDoActionModifySerialize(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ToDoAction
#         fields = ('id', 'title', 'description')
