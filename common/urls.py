from django.urls import path
from common import views

urlpatterns = [
    path('handle_slider_form/', views.SliderFormEmailView.as_view(), name="handle_slider_form"),
    path('handle_services_form/', views.ServicesFormEmailView.as_view(), name="handle_services_form"),
    path('handle_appointment_form/', views.AppointmentPopupFormEmailView.as_view(), name="handle_appointment_form"),
    path('handle_contact_form/', views.ContactFormEmailView.as_view(), name="handle_contact_form"),
    path('handle_services_appointment_form/', views.ServicesAppointmentFormEmailView.as_view(),
         name="handle_services_appointment_form"),
    path('handle_popup_form/', views.PopupFormEmailView.as_view(), name="handle_popup_form"),
]
