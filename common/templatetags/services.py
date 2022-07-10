from django import template

from female.models import FemaleServicesPageSeo, FemaleServiceItem, FemaleServiceCategory
from male.models import MaleServicesPageSeo, MaleServiceItem, MaleServiceCategory

register = template.Library()


@register.simple_tag
def get_services_seo_obj(gender):
    models = {
        "male": MaleServicesPageSeo,
        "female": FemaleServicesPageSeo
    }
    return models.get(gender).objects.first()


@register.simple_tag
def get_service_categories(gender, limit=None, in_navbar=False, in_home=False):
    models = {
        "male": MaleServiceCategory,
        "female": FemaleServiceCategory
    }
    model = models.get(gender, MaleServiceCategory)
    query = model.objects.all()
    if in_navbar:
        query = query.filter(in_navbar=True)
    if in_home:
        query = query.filter(in_home=True)
    if limit:
        return query[:limit]
    return query


@register.simple_tag
def get_services(gender, limit=None):
    models = {
        "male": MaleServiceItem,
        "female": FemaleServiceItem
    }
    model = models.get(gender)
    query = model.objects.all()
    if limit:
        return query[:limit]
    return query

@register.simple_tag
def get_home_services(gender):
    models = {
        "male": MaleServiceItem,
        "female": FemaleServiceItem
    }
    model = models.get(gender)
    if not model:
        return []
    return model.objects.filter(in_home=True)
