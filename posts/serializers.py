from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    onwer = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image')

    def get_is_owner(self, obj):
        request = self.content['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'id'
            'created_at',
            'updated_at',
            'title',
            'content',
            'image'
        ]
