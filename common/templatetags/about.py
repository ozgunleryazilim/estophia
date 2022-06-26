from django import template

from female.models import FemaleAboutPageSeo
from male.models import MaleAboutPageSeo

register = template.Library()


@register.simple_tag
def get_about_seo_obj(gender):
    models = {
        "male": MaleAboutPageSeo,
        "female": FemaleAboutPageSeo
    }
    return models.get(gender).objects.first()
