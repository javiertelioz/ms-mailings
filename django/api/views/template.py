from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters

from mailings.models import Template
from api.serializers import TemplateSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows template to be viewed.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #allowed_methods = ['GET', 'OPTIONS']

    queryset = Template.objects.filter()
    serializer_class = TemplateSerializer

    filter_backends = (
        SearchFilter,
        filters.OrderingFilter,
        filters.QueryParameterValidationFilter,
        django_filters.DjangoFilterBackend,
    )

    filterset_fields = {
        'status': ('contains', ),
        'name': ('iexact', 'contains'),
        'description': ('iexact', 'contains'),
        'subject': ('iexact', 'contains'),
        'content': ('iexact', 'contains'),
    }

    search_fields = ('name',)
    #ordering = ('-id',)
    ordering_fields = ('name',)
