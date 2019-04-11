from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters

from mailings.models import Mail
from api.serializers import MailSerializer

class MailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows mail system log to be viewed.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #allowed_methods = ['GET', 'POST', 'OPTIONS']

    queryset = Mail.objects.filter()
    serializer_class = MailSerializer

    filter_backends = (
        SearchFilter,
        filters.OrderingFilter,
        filters.QueryParameterValidationFilter,
        django_filters.DjangoFilterBackend,
    )

    filterset_fields = {
        'id': ('exact', 'in'),
        'params': ('contains', )
        #'template': ('exact', ),
    }

    search_fields = ('id', 'template', )
    ordering = ('-created_at',)
    ordering_fields = ('id', 'created_at',)

    # def create(self, validated_data):

    #     user = self.get_object()

    #     serializer = MailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         #user.set_password(serializer.data['password'])
    #         #user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

