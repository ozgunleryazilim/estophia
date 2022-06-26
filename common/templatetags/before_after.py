from django import template

from female.models import FemaleBeforeAfterPageSeo
from male.models import MaleBeforeAfterPageSeo

register = template.Library()


@register.simple_tag
def get_beforeafter_seo_obj(gender):
    models = {
        "male": MaleBeforeAfterPageSeo,
        "female": FemaleBeforeAfterPageSeo
    }
    return models.get(gender).objects.first()
