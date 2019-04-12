import json
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_json_api import filters
from rest_framework_json_api import django_filters
from django.utils.translation import gettext_lazy as _

from mailings.models import Template, Mail, PostalSystem
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

    def create(self, request, *args, **kargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            data = request.data
            tpl = Template.objects.get(pk=data['template'].get('id'))
            status = False
            request_params = json.loads(data['params'])

            try:
                mail_system = PostalSystem(tpl, request_params)
                mail_system.send([data['to']])
                status = True

            except Exception as e:
                return Response({'message': str(e)})

            mail = Mail.objects.create(
                to=data['to'],
                params=data['params'],
                template=tpl,
                status=status
            )

            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    #     user = self.get_object()

    #     serializer = MailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         #user.set_password(serializer.data['password'])
    #         #user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

