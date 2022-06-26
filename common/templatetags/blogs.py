import random

from django import template
from django.conf import settings

from female.models import FemaleServicesPageSeo, FemaleServiceItem, FemaleBlogsPageSeo, FemaleBlogCategory, FemaleBlog
from male.models import MaleServicesPageSeo, MaleServiceItem, MaleBlogsPageSeo, MaleBlogCategory, MaleBlog

register = template.Library()


@register.simple_tag
def get_blogs_seo_obj(gender):
    models = {
        "male": MaleBlogsPageSeo,
        "female": FemaleBlogsPageSeo
    }
    return models.get(gender).objects.first()


@register.simple_tag
def get_blog_categories(gender):
    models = {
        "male": MaleBlogCategory,
        "female": FemaleBlogCategory
    }
    model = models.get(gender)
    return model.objects.all()


@register.simple_tag
def get_popular_blogs(gender, number=4):
    models = {
        "male": MaleBlog,
        "female": FemaleBlog
    }
    model = models.get(gender)
    return model.objects.order_by('-view_count')[:number]


@register.simple_tag
def get_random_blogs(gender, category=None, blog=None, count=1, single=False, has_image=False):
    models = {
        "male": MaleBlog,
        "female": FemaleBlog
    }
    model = models.get(gender)
    blogs = model.objects.all()
    if has_image:
        blogs = blogs.filter(image__isnull=False)
    if blog:
        blogs = blogs.exclude(id=blog.id)
    if category and getattr(settings, "GET_RANDOM_BLOG_BY_CATEGORY", True):
        query = blogs.filter(category=category)
        blogs = query if query.exists() else blogs
    blogs = list(blogs)
    if single:
        return random.choice(blogs)
    count = count if len(blogs) > count else len(blogs)
    return random.sample(blogs, count)
