from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from male.models import MaleServiceItem, MaleBlog, MaleServiceCategory
from utils.sitemaps import ModelSitemap


class MaleStaticViewSitemap(Sitemap):
    i18n = True
    changefreq = "daily"
    priority = 1.0

    def items(self):
        view_names = ['home', 'about', 'services', 'service_categories', 'howitworks', 'before_after', 'blog_list',
                      'contact', 'kvkk']
        return [f"female:{view_name}" for view_name in view_names]

    def location(self, item):
        return reverse(item)


class MaleServiceCategorySitemap(ModelSitemap):
    model = MaleServiceCategory
    changefreq = "daily"
    priority = 0.7


class MaleServiceSitemap(ModelSitemap):
    model = MaleServiceItem
    changefreq = "daily"
    priority = 0.7


class MaleBlogSitemap(ModelSitemap):
    model = MaleBlog
    changefreq = "daily"
    priority = 0.7
