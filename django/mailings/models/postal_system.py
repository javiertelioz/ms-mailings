from django.conf import settings
from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template, Context, engines
from django.utils.translation import gettext_lazy as _

from mailings.models import Template as Tpl

class PostalSystem():

    _template_id_or_name = None
    _params = None
    _template = None

    def __init__(self, template_id_or_name, params = {}):

        self._template_id_or_name = template_id_or_name
        self._params = params

        self.django_engine = engines['django']

        self.__load_template()

    def send(self, to, bcc = []):

        try:
            email = EmailMessage(
                self.__get_message_subject(),
                self.__get_message_body(),
                self.__get_message_email_from(),
                to
            )

            email.content_subtype = "html"
            email.send()

            return email

        except Exception as e:
            raise ValueError(_("Error to send mail: %s" % str(e)))

    def __load_template(self):

        try:
            if str(self._template_id_or_name).isdigit():
                self._template = Tpl.objects.get(pk=self._template_id_or_name, status=True)
            else:
                self._template = Tpl.objects.get(name=self._template_id_or_name, status=True)

        except ObjectDoesNotExist:
            raise ValueError(_('There was an error getting template: "%s"' % self._template_id_or_name))

    def __get_message_email_from(self):

        return self._template.mailing.email

    def __get_message_subject(self):

        return self.__parse_vars(self._template.subject)

    def __get_message_body(self):

        return self.__parse_vars(
            self._template.brand.header_content +
            self._template.content +
            self._template.brand.footer_content
        )

    def __parse_vars(self, html):

        template_str = self.django_engine.from_string(html)

        return template_str.render(self._params)


# subject = 'Thank you for registering to our site'
# message = ' it  means a world to us '
# email_from = settings.EMAIL_HOST_USER
# recipient_list = ['javiertelio@siclo.com',]
# EmailMessage( subject, message, email_from, recipient_list )
#context = {'current_city': 'London'}
#db_template = Template('the current city is: {{current_city}}') # get from db
#context['content'] = db_template.render(Context(context))
