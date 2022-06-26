from django import template
from male.models import MaleHomePageSeo, MaleHomeSlider, MaleHomeDepartment
from female.models import FemaleHomePageSeo, FemaleHomeSlider, FemaleHomeDepartment

register = template.Library()


@register.simple_tag
def get_home_seo_obj(gender):
    models = {
        "male": MaleHomePageSeo,
        "female": FemaleHomePageSeo
    }
    return models.get(gender).objects.first()


@register.simple_tag
def get_home_sliders(gender):
    models = {
        "male": MaleHomeSlider,
        "female": FemaleHomeSlider
    }
    return models.get(gender).objects.all()


@register.simple_tag
def get_home_departments(gender):
    models = {
        "male": MaleHomeDepartment,
        "female": FemaleHomeDepartment
    }
    return models.get(gender).objects.all()
