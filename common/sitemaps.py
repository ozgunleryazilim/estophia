from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class CommonStaticViewSitemap(Sitemap):
    i18n = True
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['gender_selection']

    def location(self, item):
        return reverse(item)
