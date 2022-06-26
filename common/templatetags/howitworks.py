from django import template

from female.models import FemaleHowitworksPageSeo
from male.models import MaleHowitworksPageSeo

register = template.Library()


@register.simple_tag
def get_howitworks_seo_obj(gender):
    models = {
        "male": MaleHowitworksPageSeo,
        "female": FemaleHowitworksPageSeo
    }
    return models.get(gender).objects.first()
