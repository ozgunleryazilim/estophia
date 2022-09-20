from django import template

from common.models import GenderSelectionPageSeo

register = template.Library()


@register.simple_tag
def get_genderselection_seo_obj():
    return GenderSelectionPageSeo.objects.first()
