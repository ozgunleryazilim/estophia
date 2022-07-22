from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from parler.views import TranslatableSlugMixin

from utils.recaptcha import validate_recaptcha, RecaptchaValidationError
from utils.views import PaginatedListViewMixin, GenderedViewMixin, TranslatableDetailViewMixin, CategoriedListView, \
    DetailListView, HandleEmailFormView


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


class BaseBeforeAfterListView(GenderedViewMixin, PaginatedListViewMixin, CategoriedListView):
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


class BaseSearchView(View):
    blog_model = None
    service_model = None
    paginate_by = 10
    template_name = "pages/search_results.html"
    gender = ""

    def get(self, request):
        search_text = request.GET.get('search', "")
        services = self.service_model.objects.all()
        blogs = self.blog_model.objects.all()
        for word in search_text.split(" "):
            services = services.filter(
                Q(translations__title__icontains=word) |
                Q(translations__content__icontains=word)
            )
            blogs = blogs.filter(
                Q(translations__title__icontains=word) |
                Q(translations__content__icontains=word)
            )
        services = services.distinct()[:self.paginate_by]
        blogs = blogs.distinct()[:self.paginate_by]
        context = {
            'services': services,
            'blogs': blogs,
            'gender': self.gender,
        }
        return render(request, self.template_name, context)


class SliderFormEmailView(HandleEmailFormView):
    subject = "Estophia - Ansayfa Slider formu dolduruldu: {name}"
    email_template_name = "emailtemps/home_slider_form.html"
    form_identifier = "slider-form"

    def get_email_context(self, request):
        return {
            "gender": request.POST.get('gender', ""),
            "name": request.POST.get('name', ""),
            "email": request.POST.get('email', ""),
            "treatment": request.POST.get('treatment-selection', ""),
            "full_phone_number": request.POST.get('contact-full_number', ""),
            "phone": request.POST.get('phone', ""),
            "message": request.POST.get('message', "")
        }


class ServicesFormEmailView(HandleEmailFormView):
    subject = "Estophia - Servisler sayfası iletişim formu dolduruldu: {name}"
    email_template_name = "emailtemps/services_form.html"
    form_identifier = "services-form"

    def get_email_context(self, request):
        return {
            "gender": request.POST.get('gender', ""),
            "name": request.POST.get('name', ""),
            "email": request.POST.get('email', ""),
            "treatment": request.POST.get('treatment-selection', ""),
            "full_phone_number": request.POST.get('contact-full_number', ""),
            "phone": request.POST.get('phone', ""),
            "message": request.POST.get('message', "")
        }


class ServicesAppointmentFormEmailView(HandleEmailFormView):
    subject = "Estophia - Servisler randevu formu dolduruldu: {name}"
    email_template_name = "emailtemps/services_appointment_form.html"
    form_identifier = "services-appointment-form"

    def get_email_context(self, request):
        return {
            "gender": request.POST.get('gender', ""),
            "name": request.POST.get('name', ""),
            "email": request.POST.get('email', ""),
            "full_phone_number": request.POST.get('contact-full_number', ""),
            "phone": request.POST.get('phone', ""),
            "message": request.POST.get('message', "")
        }


class AppointmentPopupFormEmailView(SliderFormEmailView):
    subject = "Estophia - Randevu formu dolduruldu: {name}"
    email_template_name = "emailtemps/appointment_popup_form.html"
    form_identifier = "appointment-popup-form"
