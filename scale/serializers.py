from rest_framework import serializers
from .models import SiteActivity

class SiteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteActivity
        fields = '__all__'