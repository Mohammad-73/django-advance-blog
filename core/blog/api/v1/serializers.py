from rest_framework import serializers
from ...models import Post, Category

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(  )
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_rul = serializers.SerializerMethodField(method_name='get_abs_url')
    # category = serializers.SlugRelatedField(many=False,field='name',queryset=Category.objects.all())
    category = CategorySerializer()

    class Meta:
        model = Post
        field = ['id','author','title','content','snippet','category','status','relative_url','absolute_url','created_date','published_date']
        # read_only_fields = ['content']

    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        return super().to_representation(instance)

