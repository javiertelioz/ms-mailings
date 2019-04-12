from rest_framework_json_api import serializers

from mailings.models import Mail

class MailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mail
        fields = (
            'id',
            'template',
            'to',
            'params',
            'created_at',
        )
