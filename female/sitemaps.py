from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from female.models import FemaleServiceItem, FemaleBlog, FemaleServiceCategory
from utils.sitemaps import ModelSitemap


class FemaleStaticViewSitemap(Sitemap):
    i18n = True
    changefreq = "daily"
    priority = 1.0

    def items(self):
        view_names = ['home', 'about', 'services', 'service_categories', 'howitworks', 'before_after', 'blog_list',
                      'contact', 'kvkk']
        return [f"female:{view_name}" for view_name in view_names]

    def location(self, item):
        return reverse(item)


class FemaleServiceCategorySitemap(ModelSitemap):
    model = FemaleServiceCategory
    changefreq = "daily"
    priority = 0.7


class FemaleServiceSitemap(ModelSitemap):
    model = FemaleServiceItem
    changefreq = "daily"
    priority = 0.7


class FemaleBlogSitemap(ModelSitemap):
    model = FemaleBlog
    changefreq = "daily"
    priority = 0.7
