from django.utils.translation import ugettext_lazy as _
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

SECTION_NAME = 'common'
common = Section(SECTION_NAME)

saved_preferences = global_preferences_registry.manager()


@global_preferences_registry.register
class PhoneNumber(StringPreference):
    section = common
    name = 'phone_number'
    default = "+90 555 155 55 55"
    verbose_name = _("Telefon Numarası")


@global_preferences_registry.register
class PhoneNumber2(StringPreference):
    section = common
    name = 'phone_number2'
    default = "+90 212 155 55 55"
    verbose_name = _("Telefon Numarası 2")


@global_preferences_registry.register
class EmailAddress(StringPreference):
    section = common
    name = 'email_address'
    default = "info@estophia.com"
    verbose_name = _("Email Adresi")


@global_preferences_registry.register
class HomeHowItWorksYoutubeVideoLink(StringPreference):
    section = common
    name = 'home_howitworks_youtube_video_link'
    default = ""
    verbose_name = _("Home How It Works Youtube Video Link")

#
# @global_preferences_registry.register
# class FacebookLink(StringPreference):
#     section = page
#     name = 'facebook_link'
#     default = ""
#     verbose_name = _("Facebook Linki")
#
#
# @global_preferences_registry.register
# class InstagramLink(StringPreference):
#     section = page
#     name = 'instagram_link'
#     default = ""
#     verbose_name = _("İnstagram Linki")
#
#
# @global_preferences_registry.register
# class TwitterLink(StringPreference):
#     section = page
#     name = 'twitter_link'
#     default = ""
#     verbose_name = _("Twitter Linki")
#
#
# @global_preferences_registry.register
# class YoutubeLink(StringPreference):
#     section = page
#     name = 'youtube_link'
#     default = ""
#     verbose_name = _("Youtube Linki")
#
#
#
#
# @global_preferences_registry.register
# class Address(StringPreference):
#     section = page
#     name = 'address'
#     default = ""
#     verbose_name = _("Adres")
