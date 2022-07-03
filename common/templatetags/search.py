from django import template

from female.models import FemaleSearchPageSeo
from male.models import MaleSearchPageSeo

register = template.Library()


@register.simple_tag
def get_search_seo_obj(gender):
    models = {
        "male": MaleSearchPageSeo,
        "female": FemaleSearchPageSeo
    }
    return models.get(gender).objects.first()
