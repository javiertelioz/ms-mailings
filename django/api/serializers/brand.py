from rest_framework_json_api import serializers

from mailings.models import Brand

from .template import TemplateSerializer

class BrandSerializer(serializers.ModelSerializer):

    templates = TemplateSerializer(many=True, read_only=True)

    included_serializers = {
        'templates': TemplateSerializer,
    }

    class Meta:

        model = Brand
        fields = (
            'name',
            'logo',
            'status',
            'header_content',
            'footer_content',
            #'updated_at',
            'created_at',
            'templates'
        )
        read_only_fields = (
            'templates',
        )
