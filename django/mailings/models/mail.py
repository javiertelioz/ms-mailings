from django.utils import timezone
from django.template import Template, Context
from django.utils.translation import gettext_lazy as _

class Mail():

    """docstring for Mail"""
    def __init__(self, template_id_or_name):
        self.template_id_or_name = template_id_or_name
        self.django_engine = engines['django']
        self.__render()

    def __render(self):
        self.template = self.django_engine.from_string("Hello {{ name }}!")
        print(self.template)



#context = {'current_city': 'London'}
#db_template = Template('the current city is: {{current_city}}') # get from db
#context['content'] = db_template.render(Context(context))
