from django import template

from female.models import FemaleBeforeAfterPageSeo, FemaleBeforeAfterCategory, FemaleBeforeAfterItem
from male.models import MaleBeforeAfterPageSeo, MaleBeforeAfterCategory, MaleBeforeAfterItem

register = template.Library()


@register.simple_tag
def get_beforeafter_seo_obj(gender):
    models = {
        "male": MaleBeforeAfterPageSeo,
        "female": FemaleBeforeAfterPageSeo
    }
    return models.get(gender).objects.first()


@register.simple_tag
def get_beforeafter_categories(gender):
    models = {
        "male": MaleBeforeAfterCategory,
        "female": FemaleBeforeAfterCategory
    }
    return models.get(gender).objects.all()


@register.simple_tag
def get_beforeafter_items(gender, in_home=False, number=5):
    models = {
        "male": MaleBeforeAfterItem,
        "female": FemaleBeforeAfterItem
    }
    query = models.get(gender).objects.all()
    if in_home:
        query = query.filter(in_home=True)
    return query[:number]
