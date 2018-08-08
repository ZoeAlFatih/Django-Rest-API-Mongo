from rest_framework import serializers
from .models import Stock, Snippet
from django.contrib.auth.models import User, Group


# first we define the serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		fields = '__all__'
        

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('owner','id', 'title', 'code', 'linenos', 'language', 'style') #specific field 
        #fields = '__all__' #all field
	