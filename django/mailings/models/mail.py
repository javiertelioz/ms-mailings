from django.db.models import Q
from django.utils import timezone
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

    def send(self):

        self.__render()

    def __get_template(self):

        try:
            self.template = T.objects.filter(Q(pk=self.template_id_or_name) | Q(name=self.template_id_or_name)).first()
        except ObjectDoesNotExist:
            print("there was a error to get template")

    def __render(self):

        self.__get_template()

        html = "{}{}{}".format(
            self.template.brand.header_content,
            self.template.content,
            self.template.brand.footer_content)

        self.template = self.django_engine.from_string(html)
        print(self.template.render(self.context))





#context = {'current_city': 'London'}
#db_template = Template('the current city is: {{current_city}}') # get from db
#context['content'] = db_template.render(Context(context))
