from django.conf import settings
from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template, Context, engines
from django.utils.translation import gettext_lazy as _

from mailings.models import Template as T

class Mail():

    """docstring for Mail"""
    def __init__(self, template_id_or_name, params= {}):

        self.template_id_or_name = template_id_or_name
        self.context = params

        self.django_engine = engines['django']

        self.__get_template()

    def send(self, to, subject = ""):

        try:
            email = EmailMessage( subject, self.__parse_vars(), settings.EMAIL_HOST_USER, to )
            email.content_subtype = "html"
            email.send()

        except Exception as e:
            print("Error to send mail: %s" % str(e))

    def __get_template(self):

        try:
            if str(self.template_id_or_name).isdigit():
                self.template = T.objects.get(pk=self.template_id_or_name)
            else:
                self.template = T.objects.get(name=self.template_id_or_name)

        except ObjectDoesNotExist:
            print('There was a error to get template "%s"' % self.template_id_or_name)
            return False

    def __parse_vars(self):

        self.__get_template()

        html = "{}{}{}".format(
            self.template.brand.header_content,
            self.template.content,
            self.template.brand.footer_content
        )

        self.template = self.django_engine.from_string(html)

        return self.template.render(self.context)


# subject = 'Thank you for registering to our site'
# message = ' it  means a world to us '
# email_from = settings.EMAIL_HOST_USER
# recipient_list = ['javiertelio@siclo.com',]
# EmailMessage( subject, message, email_from, recipient_list )
#context = {'current_city': 'London'}
#db_template = Template('the current city is: {{current_city}}') # get from db
#context['content'] = db_template.render(Context(context))
