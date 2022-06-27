from django import template

from male.models import MaleKVKKPageSeo
from female.models import FemaleKVKKPageSeo

register = template.Library()


@register.simple_tag
def get_kvkk_seo_obj(gender):
    models = {
        "male": MaleKVKKPageSeo,
        "female": FemaleKVKKPageSeo
    }
    return models.get(gender).objects.first()
