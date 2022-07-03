from django.views.generic import TemplateView

from common.views import BaseServicesListView, BaseServicesDetailView, BaseBeforeAfterListView, BaseBlogListView, \
    BaseBlogDetailView, BaseServiceCategoryListView, BaseServiceCategoryDetailView, BaseSearchView
from female.forms import FemaleBlogCommentForm
from female.models import (FemaleServiceItem, FemaleBeforeAfterItem, FemaleBlog, FemaleBlogCategory,
                           FemaleServiceCategory, FemaleBeforeAfterCategory)
from utils.views import GenderedViewMixin


class FemaleHomePage(GenderedViewMixin, TemplateView):
    gender = "female"
    template_name = "pages/home.html"


class FemaleAboutPage(GenderedViewMixin, TemplateView):
    gender = "female"
    template_name = "pages/about.html"


class FemaleServiceCategoryListView(BaseServiceCategoryListView):
    gender = "female"
    model = FemaleServiceCategory


class FemaleServiceCategoryDetailView(BaseServiceCategoryDetailView):
    gender = "female"
    model = FemaleServiceCategory


class FemaleServicesListView(BaseServicesListView):
    model = FemaleServiceItem
    gender = "female"


class FemaleServicesDetailView(BaseServicesDetailView):
    gender = "female"
    model = FemaleServiceItem


class FemaleHowitworksPage(GenderedViewMixin, TemplateView):
    gender = "female"
    template_name = "pages/howitworks.html"


class FemaleBeforeAfterListView(BaseBeforeAfterListView):
    gender = "female"
    model = FemaleBeforeAfterItem
    category_model = FemaleBeforeAfterCategory


class FemaleBlogListView(BaseBlogListView):
    gender = "female"
    model = FemaleBlog
    category_model = FemaleBlogCategory


class FemaleBlogDetailView(BaseBlogDetailView):
    gender = "female"
    model = FemaleBlog
    form_class = FemaleBlogCommentForm


class FemaleContactPage(GenderedViewMixin, TemplateView):
    gender = "female"
    template_name = "pages/contact.html"


class FemaleKVKKPage(GenderedViewMixin, TemplateView):
    gender = "female"
    template_name = "pages/kvkk.html"


class FemaleSearchView(BaseSearchView):
    gender = "female"
    blog_model = FemaleBlog
    service_model = FemaleServiceItem
