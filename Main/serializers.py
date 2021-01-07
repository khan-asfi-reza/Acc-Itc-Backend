from rest_framework import serializers

from Main.models import PanelMember, PanelPost


class PanelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelPost
        fields = ('post_name', )


class PanelMemberSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    @staticmethod
    def get_post(obj):
        if obj.post:
            return obj.post.post_name
        else:
            return ""

    class Meta:
        model = PanelMember
        fields = '__all__'
