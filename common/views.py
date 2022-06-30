from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from parler.views import TranslatableSlugMixin

from utils.recaptcha import validate_recaptcha, RecaptchaValidationError
from utils.views import PaginatedListViewMixin, GenderedViewMixin, TranslatableDetailViewMixin, CategoriedListView, \
    DetailListView


class BaseServiceCategoryListView(GenderedViewMixin, PaginatedListViewMixin, ListView):
    paginate_by = 9
    template_name = "pages/service-categories.html"
    context_object_name = "categories"


class BaseServiceCategoryDetailView(TranslatableDetailViewMixin, DetailListView):
    paginate_by = 9
    template_name = "pages/service-category-detail.html"
    context_object_name = "services"
    view_url_name = "service_category_detail"

    def get_queryset(self):
        return self.object.service_items.all()


class BaseServicesListView(GenderedViewMixin, PaginatedListViewMixin, ListView):
    template_name = "pages/services.html"
    paginate_by = 9
    context_object_name = "services"


class BaseServicesDetailView(TranslatableDetailViewMixin, DetailView):
    template_name = "pages/services_detail.html"
    context_object_name = "service"
    view_url_name = "services_detail"


class BaseBeforeAfterListView(GenderedViewMixin, PaginatedListViewMixin, ListView):
    template_name = "pages/before_after.html"
    paginate_by = 9
    context_object_name = "beforeafter_list"


class BaseBlogListView(GenderedViewMixin, CategoriedListView):
    template_name = "pages/blogs.html"
    paginate_by = 9
    context_object_name = "blog_list"
    category = None


class BaseBlogDetailView(GenderedViewMixin, TranslatableSlugMixin, FormMixin, DetailListView):
    template_name = "pages/blog-details.html"
    detail_object_name = "blog"
    paginate_by = 10
    form_identifier = "comment-form"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view_count()
        return response

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_queryset(self):
        return self.object.comments.filter(is_approved=True).order_by('-created_date')

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.blog = self.object
        comment.save()
        return super().form_valid(form)

    def recaptcha_invalid(self, request):
        return redirect("{}#{}".format(request.META['HTTP_REFERER'], self.form_identifier))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())

        try:
            validate_recaptcha(request.POST)
        except RecaptchaValidationError as exc:
            messages.error(request, str(exc))
            return self.recaptcha_invalid(request)
        except Exception as e:
            print(e)
            messages.error(request, _("Mesajınız gönderilirken hata oluştu!"))
            return self.recaptcha_invalid(request)

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
