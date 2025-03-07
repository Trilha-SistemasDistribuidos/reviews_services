from rest_framework import serializers
from .models import Review
from .utils.trail_api_client import get_users # Função que busca o usuário via API

class ReviewSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()  # Campo customizado

    class Meta:
        model = Review
        fields = ['id', 'user_id', 'user_details', 'rating', 'comment', 'created_at']  # Inclui os detalhes
    
    def validate_user_id(self, value):
        if not get_users(value):
            raise serializers.ValidationError("Usuário não encontrado")
        return value
    
    def get_user_details(self, obj):
        return get_users(obj.user_id)  # Campo correto: user_id