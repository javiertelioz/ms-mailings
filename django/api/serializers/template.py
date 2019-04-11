from rest_framework_json_api import serializers

from mailings.models import Template

#from .product import ProductSerializer
class TemplateSerializer(serializers.ModelSerializer):

    #products = ProductSerializer(many=True, read_only=True)
    #branch_offices = BranchOfficeSerializer(many=True, read_only=True)

    #included_serializers = {
    #    'products': ProductSerializer,
    #    'branch_offices': BranchOfficeSerializer,
    #}

    class Meta:

        model = Template
        fields = (
            'name',
            'description',
            'subject',
            'content',
            'brand',
            #'email_from',
            'status',
            'created_at',
            #'updated_at',
        )
        # read_only_fields = (
        #     'products',
        #     #'branch_offices'
        # )
    #class JSONAPIMeta:
        #included_resources = ['products']
