from rest_framework_json_api import serializers

from mailings.models import Template

#from .product import ProductSerializer
class TemplateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Template
        fields = (
            'name',
            'description',
            'subject',
            'content',
            'brand',
            'mailing',
            'status',
            'created_at',
            'updated_at',
        )
