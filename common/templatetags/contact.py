from django import template

from male.models import MaleContactPageSeo
from female.models import FemaleContactPageSeo

register = template.Library()


@register.simple_tag
def get_contact_seo_obj(gender):
    models = {
        "male": MaleContactPageSeo,
        "female": FemaleContactPageSeo
    }
    return models.get(gender).objects.first()
